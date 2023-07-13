if ($response.statusCode != 200) {
    $done(null);
  }
  
  var body = $response.body;
  var obj = JSON.parse(body);
  var title = obj['country'] +'-'+ obj['city'];
  var ip = obj['query'];
  var subtitle = obj['as'];
  
  $done({title， ip ， subtitle});
