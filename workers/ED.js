addEventListener('fetch'， event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  // 发起远程请求
  const response = await fetch('https://sub.xf.free.hr/auto');

  // 检查请求是否成功
  if (!response.ok) {
    return new Response('Failed to fetch content', { status: response.status });
  }

  // 读取响应的内容
  const content = await response.text();

  // 对内容进行 base64 解码
  const decodedContent = atob(content);

  // 从解码后的内容中提取 @ 和 ? 之间的内容
  const extractedContent = extractContent(decodedContent);

  // 返回提取后的内容
  return new Response(extractedContent, {
    headers: { 'Content-Type': 'text/plain' }
  });
}

function extractContent(input) {
  // 使用正则表达式提取 @ 和 ? 之间的内容
  const regex = /@([^?]+)\?/g;
  const matches = [];
  let match;
  while ((match = regex.exec(input)) !== null) {
    matches.push(match[1]);
  }

  // 返回匹配到的内容，每行一个
  return matches.join('\n');
}
