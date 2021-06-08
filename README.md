## DNSUpdater

DNS自动更新程序。目前只支持阿里，后续会逐渐增加更多服务商的支持；

#### 适用场景：

一般而言我们没有固定的公网ip，很多时候重启一下路由器，都会导致我们的公网ip发生变化，导致我们无法正常访问家庭网络。在这种场景下，可以通过以下做法，来实固定ip的效果：

1. 下载该项目；

2. 配置DNSUpdater/config.json文件，其中各个字段含义如下：

   ```json
   {
       "accessKeyId": "阿里云的访问id,可以直接搜索accessKeyId到达相关页面",
       "accessSecret": "访问密钥，同上",
       "domain": "你申请下来的域名：不带前缀，比如: zhangsan.com",
       "name_ipv4": "域名的路径，比如： www, gitlab, wiki,之类"
   }
   ```

3. 用python3 的pip ，执行: `pip install -i https://pypi.douban.com/simple -r requirements.txt`

4. 执行项目： `python updater.py`