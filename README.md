# Acunetix Python API
```python

from acunetix import Acunetix

acunetix = Acunetix(host="serverip:port", api="1986ad8c0a5b3xxxxxxxxxxa2042c6ba5dc7b1ee50f71b")

# delete all targets 
acunetix.delete_all_targets()

# scan domain list 
domains = ['google.com','facebook.com','github.com']
for domain in domains:
    acunetix.start_scan(domain)


```
