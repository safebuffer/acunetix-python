target_criticality_list = {
    "critical":"10",
    "high":"20",
    "normal":"10",
    "low":"0",
}

target_criticality_allowed = list(target_criticality_list.keys())

scan_profiles_list = {
    "full_scan":"11111111-1111-1111-1111-111111111111",
    "high_risk_vuln": "11111111-1111-1111-1111-111111111112",
    "xss_vuln": "11111111-1111-1111-1111-111111111116",
    "sql_injection_vuln": "11111111-1111-1111-1111-111111111113",
    "weak_passwords": "11111111-1111-1111-1111-111111111115",
    "crawl_only": "11111111-1111-1111-1111-111111111117",
}

scan_profiles_allowed = list(scan_profiles_list.keys())