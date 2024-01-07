addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  const url1 = 'https://sub.xf.free.hr/auto';
  const response1 = await fetch(url1);
  if (!response1.ok) {
    return new Response(`Failed to fetch ${url1}`, { status: response1.status });
  }
  const text1 = await response1.text();
  const decodedText1 = atob(text1);
  const lines1 = decodedText1.split('\n');
  const filteredLines1 = lines1
    .filter(line => line.includes('SIN') || line.includes('HKG'))
    .map(line => {
      const start = line.indexOf('@');
      const end = line.indexOf('?');
      if (start !== -1 && end !== -1) {
        return line.substring(start + 1, end);
      }
      return '';
    })
    .filter(content => content.length > 0);

  const url2 = 'https://sub.cfno1.eu.org/pure';
  const response2 = await fetch(url2);
  if (!response2.ok) {
    return new Response(`Failed to fetch ${url2}`, { status: response2.status });
  }
  const text2 = await response2.text();
  const lines2 = text2.split('\n');
  const filteredAndModifiedLines2 = lines2
    .filter(line => /HK|SG/i.test(line))
    .map(line => {
      const secondCommaIndex = line.indexOf(',', line.indexOf(',') + 1);
      if (secondCommaIndex !== -1) {
        const contentBeforeSecondComma = line.substring(0, secondCommaIndex);
        return contentBeforeSecondComma.replace(/,/g, ':');
      }
      return line;
    });

  const allLines = [...filteredLines1, ...filteredAndModifiedLines2];
  const uniqueLines = [...new Set(allLines)];

  const finalText = uniqueLines.join('\n');
  return new Response(finalText, {
    headers: { 'Content-Type': 'text/plain' },
  });
}
