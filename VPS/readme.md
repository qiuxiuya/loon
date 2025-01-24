# VPS一键脚本合集(持更~)

### **欢迎大家到原作者仓库点star~**

欢迎大家来补充~

# 节点类

### 一键SS

```jsx
wget -O [ss-rust.sh](http://ss-rust.sh/) --no-check-certificate [https://raw.githubusercontent.com/xOS/Shadowsocks-Rust/master/ss-rust.sh](https://raw.githubusercontent.com/xOS/Shadowsocks-Rust/master/ss-rust.sh) && chmod +x [ss-rust.sh](http://ss-rust.sh/) && ./ss-rust.sh
```

### 一键SNELL

```jsx
wget -O [snell.sh](http://snell.sh/) --no-check-certificate [https://git.io/Snell.sh](https://git.io/Snell.sh) && chmod +x [snell.sh](http://snell.sh/) && ./snell.sh
```

### 一键TUIC

```jsx
wget -N --no-check-certificate [https://raw.githubusercontent.com/CCCOrz/auto-tuic/main/tuic.sh](https://raw.githubusercontent.com/CCCOrz/auto-tuic/main/tuic.sh) && bash [tuic.sh](http://tuic.sh/)
```

### 一键Hy2

```jsx
wget -N --no-check-certificate [https://raw.githubusercontent.com/Misaka-blog/hysteria-install/main/hy2/hysteria.sh](https://raw.githubusercontent.com/Misaka-blog/hysteria-install/main/hy2/hysteria.sh) && bash [hysteria.sh](http://hysteria.sh/)
```

### 一键MTProto(TG代理)

```jsx
apt install -y curl bash <(curl -sL [https://storage.googleapis.com/tiziblog/mt_setup.sh](https://storage.googleapis.com/tiziblog/mt_setup.sh)) ([https://storage.googleapis.com/tiziblog/mt_setup.sh](https://storage.googleapis.com/tiziblog/mt_setup.sh))
```

### 一键Singbox

```jsx
wget -N -O /root/singbox.sh https://raw.githubusercontent.com/qiuxiuya/qiuxiuya/main/VPS/singbox.sh && chmod +x /root/singbox.sh && ln -sf /root/singbox.sh /usr/local/bin/singbox && bash /root/singbox.sh
```

### 一键V2Ray(VMESS/Trojan+WS/gRPC/TCP(+TLS)

```jsx
bash <(wget -qO- -o- https://git.io/v2ray.sh)
```

                                                                                                 [GitHub](https://github.com/233boy/v2ray/tree/master)

## x-ui系列

### x-ui原版(停更了~适合新手)

```jsx
bash <(curl -Ls [https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh](https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh))
```

                                                                                                                               [GitHub](https://github.com/vaxilu/x-ui)

### sing-web/**x-ui**

```jsx
bash <(wget -qO- https://raw.githubusercontent.com/sing-web/**x**-**ui**/main/install_CN.sh)
```

GitHub

### MHSanaei/3x-ui

```jsx
bash <(curl -Ls [https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh](https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh))
```

# 工具类

### bing自签证书生成

```jsx
bash <(curl -sSL [https://raw.githubusercontent.com/qiuxiuya/qiuxiuya/main/VPS/bingcrt.sh](https://raw.githubusercontent.com/qiuxiuya/qiuxiuya/main/VPS/bingcrt.sh))
```

### 多功能工具箱

```jsx
curl -sS -O https://raw.githubusercontent.com/kejilion/sh/main/kejilion.sh && chmod +x kejilion.sh && ./kejilion.sh
```

### 一键Gost转发

```jsx
wget --no-check-certificate -O gost.sh https://raw.githubusercontent.com/KANIKIG/Multi-EasyGost/master/gost.sh && chmod +x gost.sh && ./gost.sh
```

### v4/v6优先切换

v4优先

```jsx
sed -i 's/#precedence ::ffff:0:0\/96  100/precedence ::ffff:0:0\/96  100/' /etc/gai.conf
```

v6优先

```jsx
sed -i 's/precedence ::ffff:0:0\/96  100/#precedence ::ffff:0:0\/96  100/' /etc/gai.conf
```

验证 `curl [ip.sb](http://ip.sb/)`

### 一键WARP

```jsx
wget -N [https://gitlab.com/fscarmen/warp/-/raw/main/menu.sh](https://gitlab.com/fscarmen/warp/-/raw/main/menu.sh) && bash [menu.sh](http://menu.sh/)
```

                                                                                                                               [Gitlab](https://gitlab.com/fscarmen/warp)

### 免费DNS解锁

```jsx
wget -O /tmp/lyz [http://tanainai.net/statics/bin/lyz-v0.0.3-linux-amd64](http://tanainai.net/statics/bin/lyz-v0.0.3-linux-amd64) && chmod +x /tmp/lyz && /tmp/lyz install_personal
```

                                                                                                                                  [GitHub](https://github.com/LaoYiZi-Media/unblock/wiki/%E8%80%81%E5%A7%A8%E5%AD%90%E8%A7%A3%E9%94%81)

### 一键Alist

```jsx
curl -fsSL "[https://alist.nn.ci/v3.sh](https://alist.nn.ci/v3.sh)" | bash -s install
```

                                                                                                                                [GitHub](https://github.com/alist-org/alist/tree/main)

                                                                                                                               [官方文档](https://alist.nn.ci/zh/)

### 一键ACME申请证书

```jsx
wget -N --no-check-certificate [https://raw.githubusercontent.com/Misaka-blog/acme-script/main/acme.sh](https://raw.githubusercontent.com/Misaka-blog/acme-script/main/acme.sh) && bash [acme.sh](http://acme.sh/)
```

                                                                                                                                 [GitHub](https://github.com/Misaka-blog/acme-script)

### 一键Caddy反代

```jsx
bash <(curl -L -s [https://raw.githubusercontent.com/qiuxiuya/qiuxiuya/main/VPS/caddy.sh](https://raw.githubusercontent.com/qiuxiuya/qiuxiuya/main/VPS/caddy.sh))
```

### 一键xanmod(第三方BBR

```jsx
bash <(curl -sSL [https://raw.githubusercontent.com/qiuxiuya/qiuxiuya/main/VPS/xanmod.sh](https://raw.githubusercontent.com/qiuxiuya/qiuxiuya/main/VPS/xanmod.sh))
```

按1安装后重启,然后再次运行按2

### magicTCP(魔改BBR)

```jsx
bash <(curl -sSL [https://raw.githubusercontent.com/qiuxiuya/magicTCP/main/main.sh](https://raw.githubusercontent.com/qiuxiuya/magicTCP/main/main.sh))
```

先按1安装完会自动重启，重启好再运行一次按2

### 一键BBR

```jsx
cd /usr/src && wget -N --no-check-certificate " ([https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh](https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh))[https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh](https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh)" ([https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh](https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh)) && chmod +x [tcp.sh](http://tcp.sh/) && ./tcp.sh
```

### 一键甲骨文保活

```jsx
curl -L [https://gitlab.com/spiritysdx/Oracle-server-keep-alive-script/-/raw/main/oalive.sh](https://gitlab.com/spiritysdx/Oracle-server-keep-alive-script/-/raw/main/oalive.sh) -o [oalive.sh](http://oalive.sh/) && chmod +x [oalive.sh](http://oalive.sh/) && bash [oalive.sh](http://oalive.sh/)
```

                                                                                                                              [GitHub](https://github.com/spiritLHLS/Oracle-server-keep-alive-script)

### 一键获取Root

```jsx
wget -N [https://gitlab.com/rwkgyg/vpsroot/raw/main/root.sh](https://gitlab.com/rwkgyg/vpsroot/raw/main/root.sh) && bash [root.sh](http://root.sh/)
```

### 1Panel面板(VPS管理面板)[[官网](https://1panel.cn/)]

### Debian

```jsx
curl -sSL [https://resource.fit2cloud.com/1panel/package/quick_start.sh](https://resource.fit2cloud.com/1panel/package/quick_start.sh) -o quick_start.sh && bash quick_start.sh
```

### **Ubuntu**

```jsx
curl -sSL [https://resource.fit2cloud.com/1panel/package/quick_start.sh](https://resource.fit2cloud.com/1panel/package/quick_start.sh) -o quick_start.sh && sudo bash quick_start.sh
```

### **RedHat / CentOS**

```jsx
curl -sSL [https://resource.fit2cloud.com/1panel/package/quick_start.sh](https://resource.fit2cloud.com/1panel/package/quick_start.sh) -o quick_start.sh && sh quick_start.sh
```

### 宝塔面板[[官网](https://www.bt.cn/)]

```jsx
if [ -f /usr/bin/curl ];then curl -sSO [https://download.bt.cn/install/install_panel.sh;else](https://download.bt.cn/install/install_panel.sh;else) wget -O install_panel.sh [https://download.bt.cn/install/install_panel.sh;fi;bash](https://download.bt.cn/install/install_panel.sh;fi;bash) install_panel.sh ed8484bec
```

### 一键DD

```jsx
wget --no-check-certificate -qO InstallNET.sh 'https://raw.githubusercontent.com/leitbogioro/Tools/master/Linux_reinstall/InstallNET.sh' && chmod a+x InstallNET.sh && bash InstallNET.sh -debian 11 -pwd 密码
```

### Sub-Store

```jsx
curl -sSL [https://sub-store-org.github.io/resource/ssm/install.sh](https://sub-store-org.github.io/resource/ssm/install.sh) | bash
```

### 哪吒监控面板

```jsx
curl -L [https://raw.githubusercontent.com/naiba/nezha/master/script/install.sh](https://raw.githubusercontent.com/naiba/nezha/master/script/install.sh) -o [nezha.sh](http://nezha.sh/) && chmod +x [nezha.sh](http://nezha.sh/) && sudo ./nezha.sh
```

### subconverter订阅转换

```jsx
docker run -d --restart=always -p 25500:25500 tindy2013/subconverter:latest
```

### Nexttrace路由测试

```jsx
bash <(curl -Ls [https://raw.githubusercontent.com/sjlleo/nexttrace/main/nt_install.sh](https://raw.githubusercontent.com/sjlleo/nexttrace/main/nt_install.sh))
```

## 检测类

### 流媒体检测(去广告版)

```jsx
bash <(curl -L -s https://raw.githubusercontent.com/1-stream/RegionRestrictionCheck/main/check.sh)
```

### 流媒体检测(带DNS解锁检测)

```jsx
bash <(curl -L -s [media.ispvps.com](http://media.ispvps.com/))
```

### 三网回程检测

```jsx
curl [https://raw.githubusercontent.com/zhanghanyun/backtrace/main/install.sh](https://raw.githubusercontent.com/zhanghanyun/backtrace/main/install.sh) -sSf | sh
```

### 三网回程速度测试

```jsx
bash <(curl -Lso- https://raw.githubusercontent.com/uxh/superspeed/master/superspeed.sh)
```

### 融合怪测试

```jsx
curl -L [https://gitlab.com/spiritysdx/za/-/raw/main/ecs.sh](https://gitlab.com/spiritysdx/za/-/raw/main/ecs.sh) -o [ecs.sh](http://ecs.sh/) && chmod +x [ecs.sh](http://ecs.sh/) && bash [ecs.sh](http://ecs.sh/)
```

## *一键封号(人形)*

### Linux版

```jsx
wget [https://raw.githubusercontent.com/TeamPGM/PagerMaid-Pyro/development/utils/install.sh](https://raw.githubusercontent.com/TeamPGM/PagerMaid-Pyro/development/utils/install.sh) -O [install.sh](http://install.sh/) && chmod +x [install.sh](http://install.sh/) && bash [install.sh](http://install.sh/)
```

### Docker版

```jsx
wget [https://raw.githubusercontent.com/TeamPGM/PagerMaid-Pyro/development/utils/docker.sh](https://raw.githubusercontent.com/TeamPGM/PagerMaid-Pyro/development/utils/docker.sh) -O [docker.sh](http://docker.sh/) && chmod +x [docker.sh](http://docker.sh/) && bash [docker.sh](http://docker.sh/)
```

### Pagermaid-Pyro 一键脚本重制版@EAlyce

```jsx
curl -O [https://raw.githubusercontent.com/EAlyce/conf/main/PagerMaid/RXsetup.sh](https://raw.githubusercontent.com/EAlyce/conf/main/PagerMaid/RXsetup.sh) && chmod +x [RXsetup.sh](http://rxsetup.sh/) && ./RXsetup.sh
```

                                                                                                                   

                                                                                                   **感谢二鸟提供了一部分一键**

                                                                                                   **感谢[猫咪](https://t.me/GetSomeCats)/[一佬](https://t.me/zhetengsha)/[薯薯](https://t.me/GetSomeFriesChannel)/[Misakablog](https://blog.misaka.rest/)**

                                                                                                   **感谢脚本原作者们的付出**

                                                                                                   **频道[https://t.me/zdqiuxiuya](https://t.me/zdqiuxiuya)**

                                                                                                         **永远爱Miku的秋咻~**