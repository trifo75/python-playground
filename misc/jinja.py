import jinja2
"""
Ez kellene legyen
mksyscfg -r lpar -m TORNADO-NODE1 -i "name=test_lpar, lpar_id=215, profile_name=normal ,lpar_env=aixlinux,min_mem=4096, desired_mem=16384, max_mem=32768, mem_mode=ded, proc_mode=shared, min_procs=1, desired_procs=2, max_procs=4, min_proc_units=0.5, desired_proc_units=1, max_proc_units=4, sharing_mode=uncap, uncap_weight=64, conn_monitoring=1, boot_mode=norm, max_virtual_slots=200,
 \"virtual_eth_adapters=2/0/998//0/0/ETHERNET0//all/none,3/0/90//0/0/ETHERNET0//all/none,4/0/12//0/0/ETHERNET0//all/none,5/0/3997//0/0/ETHERNET0//all/none\", \"virtual_fc_adapters=10/client//TORNADO-VIO1/2150//0,11/client//TORNADO-VIO2/2151//0,12/client//TORNADO-VIO1/2152//0,13/client//TORNADO-VIO2/2153//0\" "
és helyette ez jon ki
mksyscfg -r lpar -m TORNADO-NODE1 -i "name=test_lpar, lpar_id=215, profile_name=normal ,lpar_env=aixlinux,min_mem=4096, desired_mem=16384, max_mem=32768, mem_mode=ded, proc_mode=shared, min_procs=1, desired_procs=2, max_procs=4, min_proc_units=0.5, desired_proc_units=1, max_proc_units=4, sharing_mode=uncap, uncap_weight=64, conn_monitoring=1, boot_mode=norm, max_virtual_slots=200, 
"virtual_eth_adapters=2/0/998//0/0/ETHERNET0//all/none,3/0/90//0/0/ETHERNET0//all/none,4/0/12//0/0/ETHERNET0//all/none,5/0/3997//0/0/ETHERNET0//all/none", "virtual_fc_adapters=10/client//TORNADO-VIO1/2150//0,11/client//TORNADO-VIO2/2151//0,12/client//TORNADO-VIO1/2152//0,13/client//TORNADO-VIO2/2153//0" "
"""

LPAR_template = '''
# LPAR profilok létrehozása
mksyscfg -r lpar -m {{ MANAGED_SYSTEM }} -i "name={{ LPAR_NAME }}, lpar_id={{ LPAR_ID }}, profile_name=normal ,lpar_env=aixlinux,min_mem={{ MEM_MIN }}, desired_mem={{ MEM_DES }}, max_mem={{ MEM_MAX }}, mem_mode=ded, proc_mode=shared, min_procs={{ CPU_MIN }}, desired_procs={{ CPU_DES }}, max_procs={{ CPU_MAX }}, min_proc_units={{ EC_MIN }}, desired_proc_units={{ EC_DES }}, max_proc_units={{ EC_MAX }}, sharing_mode=uncap, uncap_weight=64, conn_monitoring=1, boot_mode=norm, max_virtual_slots=200, \"virtual_eth_adapters=2/0/{{ ENT0_VLAN }}//0/0/ETHERNET0//all/none,3/0/{{ ENT1_VLAN }}//0/0/ETHERNET0//all/none,4/0/{{ ENT2_VLAN }}//0/0/ETHERNET0//all/none,5/0/{{ ENT3_VLAN }}//0/0/ETHERNET0//all/none\", \"virtual_fc_adapters=10/client//{{ VIO1 }}/{{ LPAR_ID }}0//0,11/client//{{ VIO2 }}/{{ LPAR_ID }}1//0,12/client//{{ VIO1 }}/{{ LPAR_ID }}2//0,13/client//{{ VIO2 }}/{{ LPAR_ID }}3//0\" "

# WWPN-ek kinyerése
lssyscfg -r prof -m {{ MANAGED_SYSTEM }} --filter lpar_names={{ LPAR_NAME }} -F name,virtual_fc_adapters

#Server virtual adapter-ek ltrehozása
chhwres -r virtualio -m {{ MANAGED_SYSTEM }} -o a -p {{ VIO1 }} --rsubtype fc -s {{ LPAR_ID }}0 -a "adapter_type=server,remote_lpar_name={{ LPAR_NAME }},remote_slot_num=10"
chhwres -r virtualio -m {{ MANAGED_SYSTEM }} -o a -p {{ VIO2 }} --rsubtype fc -s {{ LPAR_ID }}1 -a "adapter_type=server,remote_lpar_name={{ LPAR_NAME }},remote_slot_num=11"
chhwres -r virtualio -m {{ MANAGED_SYSTEM }} -o a -p {{ VIO1 }} --rsubtype fc -s {{ LPAR_ID }}2 -a "adapter_type=server,remote_lpar_name={{ LPAR_NAME }},remote_slot_num=12"
chhwres -r virtualio -m {{ MANAGED_SYSTEM }} -o a -p {{ VIO2 }} --rsubtype fc -s {{ LPAR_ID }}3 -a "adapter_type=server,remote_lpar_name={{ LPAR_NAME }},remote_slot_num=13"

# Változott VIO LPAR profil mentése az aktuálisan használt profilba
mksyscfg -r prof -m {{ MANAGED_SYSTEM }} -o save -p {{ VIO1 }} -n `lssyscfg -r lpar -m {{ MANAGED_SYSTEM }} --filter "lpar_names={{ VIO1 }}" -F curr_profile` --force
mksyscfg -r prof -m {{ MANAGED_SYSTEM }} -o save -p {{ VIO2 }} -n `lssyscfg -r lpar -m {{ MANAGED_SYSTEM }} --filter "lpar_names={{ VIO2 }}" -F curr_profile` --force

# cfgdev futtatása a VIO hostokon
viosvrcmd -m {{ MANAGED_SYSTEM }} -p {{ VIO1 }} -c "cfgdev -dev vio0"
viosvrcmd -m {{ MANAGED_SYSTEM }} -p {{ VIO2 }} -c "cfgdev -dev vio0"

# új vfchost device nevek lekérdezése. Ha több "NOT_LOGGED_IN" is van, akkor az lpar_id alapján lesz meg a megfelelő:
viosvrcmd -m {{ MANAGED_SYSTEM }} -p {{ VIO1 }} -c "lsmap -all -npiv -fmt : " | grep ":{{ LPAR_ID }}:"
viosvrcmd -m {{ MANAGED_SYSTEM }} -p {{ VIO2 }} -c "lsmap -all -npiv -fmt : " | grep ":{{ LPAR_ID }}:"

#NPIV mapping legyartasa - fcs0 es fcs1 van a pFlex VIO-kon
#A vfchost neveket csereld ki a lekerdezettekre!!!
viosvrcmd -m {{ MANAGED_SYSTEM }} -p {{ VIO1 }} -c "vfcmap -vadapter vfchostXX -fcp fcs0"
viosvrcmd -m {{ MANAGED_SYSTEM }} -p {{ VIO1 }} -c "vfcmap -vadapter vfchostXX_ -fcp fcs3"
viosvrcmd -m {{ MANAGED_SYSTEM }} -p {{ VIO2 }} -c "vfcmap -vadapter vfchostXX -fcp fcs0"
viosvrcmd -m {{ MANAGED_SYSTEM }} -p {{ VIO2 }} -c "vfcmap -vadapter vfchostXX -fcp fcs3"
'''

demo_input = '''
mksyscfg -r lpar -m {{ MANAGED_SYSTEM }} -i "name={{ LPAR_NAME }}, lpar_id={{ LPAR_ID }}, \"virtual_eth_adapters=2/0/{{ ENT0_VLAN }}//0/0/ETHERNET0//all/none,3/0/{{ ENT1_VLAN }}//0/0/ETHERNET0//all/none,4/0/{{ ENT2_VLAN }}//0/0/ETHERNET0//all/none,5/0/{{ ENT3_VLAN }}//0/0/ETHERNET0//all/none\", \"virtual_fc_adapters=10/client//{{ VIO1 }}/{{ LPAR_ID }}0//0,11/client//{{ VIO2 }}/{{ LPAR_ID }}1//0,12/client//{{ VIO1 }}/{{ LPAR_ID }}2//0,13/client//{{ VIO2 }}/{{ LPAR_ID }}3//0\" "

'''
# LPAR konfig
lpar_config={
    "LPAR_ID" : "215",
    "LPAR_NAME" : "test_lpar",
    "EC_MIN" : "0.5",    # Entitled capacity params
    "EC_DES" : "1",
    "EC_MAX" : "4",
    "CPU_MIN" : "1",     # VCPU params
    "CPU_DES" : "2",
    "CPU_MAX" : "4",
    "MEM_MIN" : "4096",  # MEM params
    "MEM_DES" : "16384",
    "MEM_MAX" : "32768",
    "MANAGED_SYSTEM" : "TORNADO-NODE1",
    "VIO1" : "TORNADO-VIO1",
    "VIO2" : "TORNADO-VIO2",
    "ENT0_VLAN" : "46",    # management
    "ENT1_VLAN" : "88",    # backup
    "ENT2_VLAN" : "123",   # service
    "ENT3_VLAN" : "1697",  # RAC internal
}

environement = jinja2.Environment()

template = environement.from_string(LPAR_template)
out = template.render(lpar_config)

demo_template = environement.from_string(demo_input)
demo_out = demo_template.render(lpar_config)

#print(out) # megkimeljuk a kozonseget a scripttol
print(demo_out)

