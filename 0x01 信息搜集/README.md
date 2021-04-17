
![信息收集](https://github.com/aplyc1a/toolkits/blob/master/0x01 信息搜集/信息收集.png)

**图示说明**：

| 编号 | 脚本                                                         | 说明                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [1]  | -                                                            | 暂缺                                                         |
| [2]  | -                                                            | 暂缺                                                         |
| [3]  | info-ip-section.py                                           | 用于将多种格式的IP资产转化为IP列表                           |
| [4]  | cat urls-ip.txt\|awk -F/ '{print $3}'\|grep "^[0-9]"         | 用于从urls中截取出所有的IP                                   |
| [5]  | cat urls-ip.txt\|awk -F/ '{print $3}'\|grep -v "^[0-9]"      | 用于从url清单中截取出所有的域名                              |
| [6]  | info_checkalive.py                                           | 单线程url资产存活型检查                                      |
| [7]  | cat ip.txt\|awk -F. '{print  $1"."$2"."$3".0/24"}'\|sort\|uniq | 依据IP获得C段，得到的结果用info-ip-section.py 处理可以再得到所有的C段IP。 |
| [8]  | batch_ping.sh                                                | 对host进行ping存活性检查。                                   |
| [9]  | info-dnsdigger.py                                            | 使用dig获取所有类型的DNS记录。<br>这种方式是不全的，建议使用字典穷举工具（subDomainsBrute、挖掘机）、域名历史解析记录数据库（dnsgrep.cn） |

