var url = "http://ip-api.com/json/?fields=28191&lang=zh-CN";
var inputParams = $environment.params;
var nodeName = inputParams.node;

var requestParams = {
    url:url,
    node:nodeName
}

var message = ""

const paras = ["query","country","regionName","city","org","isp","as"];
const paran = ["落 地 I P ","落地国家","落地地区","落地城市","落地机构","落地 ISP","落地ASN"];

$httpClient.get(requestParams, (error, response, data) => {
    if (error) {
        message = "</br>** 查询超时 **"
        message = `<p style="text-align: center; font-family: -apple-system; font-size: 15px;color:#ff0000;font-weight: bold;">` + message + `</p>`
        $done({"title": "落地检测", "htmlMessage": message});
    } else {
        console.log(data);
        message = data ? json2info(data, paras) : "";
        $done({"title": "落地检测", "htmlMessage": message});
    }
})

function json2info(cnt, paras) {
    var res = "------------------------------------";
    cnt = JSON.parse(cnt);
    //console.log(cnt);
    for (i = 0;i < paras.length; i ++) {
        cnt[paras[i]] = paras[i] == "country" ? cnt[paras[i]] + " " + cnt["countryCode"] : cnt[paras[i]];
        cnt[paras[i]] = paras[i] == "regionName" ? cnt[paras[i]] + " " + cnt["region"] : cnt[paras[i]];

        res = cnt[paras[i]] ? res + "</br><b>" + "<font  color=>" + paran[i] + "</font> : " + "</b>"+ "<font  color=>" + cnt[paras[i]] + "</font></br>" : res;
    }

   res = `<p style="text-align: left; font-family: -apple-system; font-size: large; font-weight: thin">` + res + "------------------------------------" + "</br>" + "<font color=#ff0000>" + "<b>检测节点</b> ➟ " + $environment.params.node + "</font></p>";
   return res;
}