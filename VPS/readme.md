# VPS一键脚本合集(持更~)

### **大家到原作者仓库点star~**

### 一键SS

```
wget -O [ss-rust.sh](http://ss-rust.sh/) --no-check-certificate [https://raw.githubusercontent.com/xOS/Shadowsocks-Rust/master/ss-rust.sh](https://raw.githubusercontent.com/xOS/Shadowsocks-Rust/master/ss-rust.sh) && chmod +x [ss-rust.sh](http://ss-rust.sh/) && ./ss-rust.sh
```

### 一键SNELL

```
wget -O [snell.sh](http://snell.sh/) --no-check-certificate [https://git.io/Snell.sh](https://git.io/Snell.sh) && chmod +x [snell.sh](http://snell.sh/) && ./snell.sh
```

### 一键Hy2

```
wget -N --no-check-certificate [https://raw.githubusercontent.com/Misaka-blog/hysteria-install/main/hy2/hysteria.sh](https://raw.githubusercontent.com/Misaka-blog/hysteria-install/main/hy2/hysteria.sh) && bash [hysteria.sh](http://hysteria.sh/)
```

### 一键Singbox

```
wget -N -O /root/singbox.sh https://raw.githubusercontent.com/qiuxiuya/qiuxiuya/main/VPS/singbox.sh && chmod +x /root/singbox.sh && ln -sf /root/singbox.sh /usr/local/bin/singbox && bash /root/singbox.sh
```

### 一键V2Ray(VMESS/Trojan+WS/gRPC/TCP(+TLS)

```
bash <(wget -qO- -o- https://git.io/v2ray.sh)
```

## x-ui系列

### x-ui原版(停更了~适合新手)

```
bash <(curl -Ls [https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh](https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh))
```

### sing-web/**x-ui**

```
bash <(wget -qO- https://raw.githubusercontent.com/sing-web/**x**-**ui**/main/install_CN.sh)
```

### kejilion工具箱

```
curl -sS -O https://raw.githubusercontent.com/kejilion/sh/main/kejilion.sh && chmod +x kejilion.sh && ./kejilion.sh
```

### MHSanaei/3x-ui

```
bash <(curl -Ls [https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh](https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh))
```

### Gost转发

```
wget --no-check-certificate -O gost.sh https://raw.githubusercontent.com/KANIKIG/Multi-EasyGost/master/gost.sh && chmod +x gost.sh && ./gost.sh
```

### v4/v6优先切换

v4优先

```
sed -i 's/#precedence ::ffff:0:0\/96  100/precedence ::ffff:0:0\/96  100/' /etc/gai.conf
```

v6优先

```
sed -i 's/precedence ::ffff:0:0\/96  100/#precedence ::ffff:0:0\/96  100/' /etc/gai.conf
```

验证 `curl ip.sb`

### 一键WARP

```
wget -N [https://gitlab.com/fscarmen/warp/-/raw/main/menu.sh](https://gitlab.com/fscarmen/warp/-/raw/main/menu.sh) && bash [menu.sh](http://menu.sh/)
```

### 免费DNS解锁

```
wget -O /tmp/lyz [http://tanainai.net/statics/bin/lyz-v0.0.3-linux-amd64](http://tanainai.net/statics/bin/lyz-v0.0.3-linux-amd64) && chmod +x /tmp/lyz && /tmp/lyz install_personal
```

### 一键Alist

```
curl -fsSL "[https://alist.nn.ci/v3.sh](https://alist.nn.ci/v3.sh)" | bash -s install
```

### 一键ACME申请证书

```
wget -N --no-check-certificate [https://raw.githubusercontent.com/Misaka-blog/acme-script/main/acme.sh](https://raw.githubusercontent.com/Misaka-blog/acme-script/main/acme.sh) && bash [acme.sh](http://acme.sh/)
```

### 一键安装Caddy反代

```
bash <(curl -L -s [https://raw.githubusercontent.com/qiuxiuya/qiuxiuya/main/VPS/caddy.sh](https://raw.githubusercontent.com/qiuxiuya/qiuxiuya/main/VPS/caddy.sh))
```

### magicTCP(魔改BBR)

```
bash <(curl -sSL [https://raw.githubusercontent.com/qiuxiuya/magicTCP/main/main.sh](https://raw.githubusercontent.com/qiuxiuya/magicTCP/main/main.sh))
```

先按1安装完会自动重启，重启好再运行一次按2

### 一键BBR

```
cd /usr/src && wget -N --no-check-certificate " ([https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh](https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh))[https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh](https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh)" ([https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh](https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh)) && chmod +x [tcp.sh](http://tcp.sh/) && ./tcp.sh
```

### 一键甲骨文保活

```
curl -L [https://gitlab.com/spiritysdx/Oracle-server-keep-alive-script/-/raw/main/oalive.sh](https://gitlab.com/spiritysdx/Oracle-server-keep-alive-script/-/raw/main/oalive.sh) -o [oalive.sh](http://oalive.sh/) && chmod +x [oalive.sh](http://oalive.sh/) && bash [oalive.sh](http://oalive.sh/)
```

### 一键获取Root

```
wget -N [https://gitlab.com/rwkgyg/vpsroot/raw/main/root.sh](https://gitlab.com/rwkgyg/vpsroot/raw/main/root.sh) && bash [root.sh](http://root.sh/)
```

### 1Panel面板(VPS管理面板)[[官网](https://1panel.cn/)]

### Debian

```
curl -sSL [https://resource.fit2cloud.com/1panel/package/quick_start.sh](https://resource.fit2cloud.com/1panel/package/quick_start.sh) -o quick_start.sh && bash quick_start.sh
```

### **Ubuntu**

```
curl -sSL [https://resource.fit2cloud.com/1panel/package/quick_start.sh](https://resource.fit2cloud.com/1panel/package/quick_start.sh) -o quick_start.sh && sudo bash quick_start.sh
```

### **RedHat / CentOS**

```
curl -sSL [https://resource.fit2cloud.com/1panel/package/quick_start.sh](https://resource.fit2cloud.com/1panel/package/quick_start.sh) -o quick_start.sh && sh quick_start.sh
```

### 宝塔面板[[官网](https://www.bt.cn/)]

```
if [ -f /usr/bin/curl ];then curl -sSO [https://download.bt.cn/install/install_panel.sh;else](https://download.bt.cn/install/install_panel.sh;else) wget -O install_panel.sh [https://download.bt.cn/install/install_panel.sh;fi;bash](https://download.bt.cn/install/install_panel.sh;fi;bash) install_panel.sh ed8484bec
```

### 一键DD

```
wget --no-check-certificate -qO InstallNET.sh 'https://raw.githubusercontent.com/leitbogioro/Tools/master/Linux_reinstall/InstallNET.sh' && chmod a+x InstallNET.sh && bash InstallNET.sh -debian 11 -pwd 密码
```

### Sub-Store

```
curl -sSL [https://sub-store-org.github.io/resource/ssm/install.sh](https://sub-store-org.github.io/resource/ssm/install.sh) | bash
```

### 哪吒监控面板

```
curl -L [https://raw.githubusercontent.com/naiba/nezha/master/script/install.sh](https://raw.githubusercontent.com/naiba/nezha/master/script/install.sh) -o [nezha.sh](http://nezha.sh/) && chmod +x [nezha.sh](http://nezha.sh/) && sudo ./nezha.sh
```

### subconverter订阅转换

```
docker run -d --restart=always -p 25500:25500 tindy2013/subconverter:latest
```

### Nexttrace路由测试

```
bash <(curl -Ls [https://raw.githubusercontent.com/sjlleo/nexttrace/main/nt_install.sh](https://raw.githubusercontent.com/sjlleo/nexttrace/main/nt_install.sh))
```

### 流媒体检测(去广告版)

```
bash <(curl -L -s https://raw.githubusercontent.com/1-stream/RegionRestrictionCheck/main/check.sh)
```

### 流媒体检测(带DNS解锁检测)

```
bash <(curl -L -s [media.ispvps.com](http://media.ispvps.com/))
```

### 三网回程检测

```
curl [https://raw.githubusercontent.com/zhanghanyun/backtrace/main/install.sh](https://raw.githubusercontent.com/zhanghanyun/backtrace/main/install.sh) -sSf | sh
```

### 三网回程速度测试

```
bash <(curl -Lso- https://raw.githubusercontent.com/uxh/superspeed/master/superspeed.sh)
```

### 融合怪测试

```
curl -L [https://gitlab.com/spiritysdx/za/-/raw/main/ecs.sh](https://gitlab.com/spiritysdx/za/-/raw/main/ecs.sh) -o [ecs.sh](http://ecs.sh/) && chmod +x [ecs.sh](http://ecs.sh/) && bash [ecs.sh](http://ecs.sh/)
```

## *一键封号(人形)*

### Linux版

```
wget [https://raw.githubusercontent.com/TeamPGM/PagerMaid-Pyro/development/utils/install.sh](https://raw.githubusercontent.com/TeamPGM/PagerMaid-Pyro/development/utils/install.sh) -O [install.sh](http://install.sh/) && chmod +x [install.sh](http://install.sh/) && bash [install.sh](http://install.sh/)
```

### Docker版

```
wget [https://raw.githubusercontent.com/TeamPGM/PagerMaid-Pyro/development/utils/docker.sh](https://raw.githubusercontent.com/TeamPGM/PagerMaid-Pyro/development/utils/docker.sh) -O [docker.sh](http://docker.sh/) && chmod +x [docker.sh](http://docker.sh/) && bash [docker.sh](http://docker.sh/)
```

### Pagermaid-Pyro 一键脚本重制版@EAlyce

```
curl -O [https://raw.githubusercontent.com/EAlyce/conf/main/PagerMaid/RXsetup.sh](https://raw.githubusercontent.com/EAlyce/conf/main/PagerMaid/RXsetup.sh) && chmod +x [RXsetup.sh](http://rxsetup.sh/) && ./RXsetup.sh
```
