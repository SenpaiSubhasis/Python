def ipaddress(ip):
  if len(ip)<0:
    return False
 
  if "." in ip:
    ip_split = ip.split(".")
  elif ":":
    ip_split = ip.split(":")
  else:
    return False
      
   
  for x in ip_split:
    if hex(int(x))or int(x)<=255:
        continue
        print("ipv4")
    else:
      ipv6 = hex(int(x))
      print("ipv6")
      continue


ans = ipaddress(" 2001:0db8:85a3:0:0:8A2E:0370:7334")
print(ans)