<h1 align="center">&#127978;OSSCS</h1>
<p align="center">
<img src="https://img.shields.io/github/last-commit/zivenyang/osscs" alt="Last commit">
  <img src="https://img.shields.io/github/downloads/zivenyang/osscs/total" alt="Downloads">
  <a href="https://github.com/zivenyang/osscs/blob/main/LICENSE"><img src="https://img.shields.io/github/license/zivenyang/osscs" alt="License"></a>
</p>

>开源软件便利店（Open Source Software Convenience Stores），用于快速挑选安全新鲜的开源软件。


## 前言
本项目是一款开源软件选型应用，旨在让用户能够快速挑选长期维护、社区活跃、安全性高的开源软件。  
本项目也是一个python全栈项目，前端使用Vue3.0+Antdv，后端使用djiango4.0+DRF，同时使用Gihub Actions进行CICD。  

## 私有化部署
*本项目的在线版本将在后续上线，敬请期待*  
### 环境准备
docker安装：https://docs.docker.com/engine/install/  
docker-compose安装：https://docs.docker.com/compose/install/

### 步骤1. 注册libraries.io，获取API Key
本项目的包数据都来自[libraries.io](https://libraries.io/api)，因此需要[注册](https://libraries.io/account)来获取接口访问权限   
用户登录后在[账户](https://libraries.io/account)页面中复制API Key

### 步骤2. 创建docker-compose.yml，并修改API Key
你可以将项目下的[docker-compose.yml](/docker-compose-local.yml)文件复制到本地，然后修改`LIBRARIES_IO_API_KEY`的值

### 步骤3. 使用docker-compose启动容器
```shell
docker-compose -f "docker-compose.yml" up -d --build
```

### 步骤4： 访问127.0.0.1:80
