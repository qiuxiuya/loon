if ($response.statusCode != 200) {
    $done(null);
  }
  
  var body = $response.body;
  var obj = JSON.parse(body);
  var title = obj['country'] + obj['city'];
  var subtitle = obj['as'];
  var ip = obj['query'];
  var description = obj['query'] + '\n' +obj['as'];
  
  $done({title, subtitle, ip, description});
