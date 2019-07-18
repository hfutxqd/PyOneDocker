# PyOneDocker
docker-compose for PyOne
使用docker-compose一键部署PyOne

## 第一步 安装docker和compose(已安装的跳过)

[docker官方安装步骤参考](https://docs.docker.com/install/)     
[compose官方安装步骤参考](https://docs.docker.com/compose/install/)     

## 第二步 下载仓库

```
git clone https://github.com/hfutxqd/PyOneDocker.git
```
## 第三步 修改配置
切换到代码目录：
```
cd PyOneDocker
```
修改self_config.py文件，最重要的是把
```
password="SetYourPassword"
```
替换成你自己的密码

### 第四步 启动PyOne
后台启动：
```
docker-compose up -d
```
前台启动(可以用来排错)
```
docker-compose up
```

### 第五步 访问PyOne
在服务器本地，你现在已经可以通过以下地址访问PyOne：
```
http://10.5.0.4:34567
```
如果你需要直接通过外部网络访问，你需要把`docker-compose.yml`文件修改为以下内容：
（把容器内的34567暴露到主机的34567）

```

version: '3'
services:
  mongo:
    image: mongo:4
    restart: always
    networks:
      net-pyone:
        ipv4_address: 10.5.0.2

  redis:
    image: redis:alpine
    restart: always
    networks:
      net-pyone:
        ipv4_address: 10.5.0.3

  py-one:
    build: .
    volumes: 
      - ./self_config.py:/root/PyOne/self_config.py
      - ./supervisord.conf:/root/PyOne/supervisord.conf
    depends_on:
      - mongo
      - redis
    restart: always
    ports:
      - 34567:34567
    networks:
      net-pyone:
        ipv4_address: 10.5.0.4
    
networks:
  net-pyone:
    driver: bridge
    ipam:
     config:
       - subnet: 10.5.0.0/16
```

我不推荐这种方式，因为其不支持https，推荐使用Apache或者Nginx把流量转发到10.5.0.4:34567，这样即可以把PyOne绑定到一个子域名，也能很好的支持Let’s Encrypt的SSL证书和证书自动更新
