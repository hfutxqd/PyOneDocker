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
