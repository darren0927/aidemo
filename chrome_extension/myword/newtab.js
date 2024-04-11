//// 定义一个词汇数组和它们的频率
//const wordsData = [
//  { text: "江忆恩", size: 20 },
//  { text: "郑永年", size: 20 },
//  { text: "施展", size: 20 },
//
//  { text: "温铁军", size: 20 },
//  { text: "卢麒元", size: 20 },
//
//  { text: "崔寒柏", size: 20 }
//  // 更多单词...
//];
//
//// 设置词云的宽度和高度
//const width = window.innerWidth;
//const height = window.innerHeight;
//
//// 创建词云布局
//const layout = d3.layout.cloud()
//  .size([width, height])
//  .words(wordsData)
//  .padding(5)
//  .rotate(0)
//  .font("Impact")
//  .fontSize(d => d.size)
//  .on("end", drawWordCloud);
//
//// 定义颜色尺度
//const color = d3.scaleOrdinal(d3.schemeCategory10);
//
//// 定义浮动动画
//function floatingAnimation(selection) {
//  selection.transition()
//    .duration(2000)
//    .ease(d3.easeLinear)
//    .attr("transform", d => {
//      const dx = (Math.random() - 0.5) * 10;
//      const dy = (Math.random() - 0.5) * 10;
//      return `translate(${[d.x + dx, d.y + dy]})rotate(${d.rotate})`;
//    })
//    .transition()
//    .duration(2000)
//    .ease(d3.easeLinear)
//    .attr("transform", d => `translate(${[d.x, d.y]})rotate(${d.rotate})`)
//    .on('end', function() { floatingAnimation(d3.select(this)); });
//}
//
//// 绘制词云的函数
//function drawWordCloud(words) {
//  // 创建一个SVG元素并附加到#wordcloud元素
//  const svg = d3.select("#wordcloud").append("svg")
//    .attr("width", width)
//    .attr("height", height)
//    .append("g")
//    .attr("transform", `translate(${width / 2},${height / 2})`);
//
//  // 创建文本元素并应用数据
//  const text = svg.selectAll("text")
//    .data(words)
//    .enter().append("text")
//    .style("font-size", d => d.size + "px")
//    .style("font-family", "Impact")
//    .style("fill", (d, i) => color(i))
//    .attr("text-anchor", "middle")
//    .attr("transform", d => `translate(${[d.x, d.y]})rotate(${d.rotate})`)
//    .text(d => d.text);
//
//  // 应用浮动动画
//  text.each(function() {
//    floatingAnimation(d3.select(this));
//  });
//}
//
//// 开启布局计算
//layout.start();

// 获取美元兑换人民币汇率
function fetchUsdToCnyRate() {
  fetch('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CNY&apikey=4MPL42O77Y97SYJJ')
    .then(response => response.json())
    .then(data => {
      let rate = parseFloat(data['Realtime Currency Exchange Rate']['5. Exchange Rate']);
      document.getElementById('usdToCnyRate').textContent = `1 USD = ${rate.toFixed(2)} CNY`;
    })
    .catch(error => {
      console.error('Error fetching USD to CNY rate:', error);
      document.getElementById('usdToCnyRate').textContent = 'Unavailable';
    });
}

// 获取BTC比特币价格
function fetchBitcoinPrice() {
  // 注意: 请将 YOUR_API_KEY 替换为你的 Alpha Vantage API 密钥
  const url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=4MPL42O77Y97SYJJ';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      // 确保你了解了 API 的正确响应结构，并更新下面的代码以匹配该结构
      const exchangeRateData = data['Realtime Currency Exchange Rate'];
      const rate = parseFloat(exchangeRateData['5. Exchange Rate']);
      document.getElementById('bitcoinPrice').textContent = `1 BTC = ${rate.toFixed(2)} USD`;
    })
    .catch(error => {
      console.error('Error fetching Bitcoin price:', error);
      document.getElementById('bitcoinPrice').textContent = 'Unavailable';
    });
}

// 获取黄金实时价格
function fetchGoldPrice(apiKey, fromCurrency, toCurrency) {
  const url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=XAU&to_currency=USD&apikey=4MPL42O77Y97SYJJ';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      // 确保你了解了 API 的正确响应结构，并更新下面的代码以匹配该结构
      const exchangeRateData = data['Realtime Currency Exchange Rate'];
      const rate = parseFloat(exchangeRateData['5. Exchange Rate']);
      document.getElementById('goldPrice').textContent = `1盎司(28.349克) = ${rate.toFixed(2)} USD`;
    })
    .catch(error => {
      console.error('Error fetching gold price:', error);
      document.getElementById('goldPrice').textContent = 'Unavailable';
    });

}

// 获取石油实时价格
function fetchWTIPrice(apiKey, fromCurrency, toCurrency) {
  const url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=WTI&to_currency=USD&apikey=4MPL42O77Y97SYJJ';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const exchangeRateData = data['Realtime Currency Exchange Rate'];
      const rate = parseFloat(exchangeRateData['5. Exchange Rate']);
      document.getElementById('WTIPrice').textContent = `1桶(WTI) = ${rate.toFixed(2)} USD`;
    })
    .catch(error => {
      console.error('Error fetching WTI price:', error);
      document.getElementById('WTIPrice').textContent = 'Unavailable';
    });

}

// 获取美国国债十年期走势
function fetch10YearTreasury(apiKey, fromCurrency, toCurrency) {
  const url = 'https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=daily&maturity=10year&apikey=4MPL42O77Y97SYJJ';

  fetch(url)
    .then(response => response.json())
    .then(data => {
          const yieldData = data['data']; // 获取数据数组
          const chartData = {
            labels: yieldData.map(item => item.date), // 日期数组
            datasets: [{
              label: '10 Year Treasury Yield',
              data: yieldData.map(item => item.value), // 收益率数组
              fill: false,
              borderColor: 'rgb(75, 192, 192)',
              tension: 0.1
            }]
          };

          const ctx = document.getElementById('treasury').getContext('2d');
          new Chart(ctx, {
            type: 'line', // 图表类型为线图
            data: chartData, // 图表数据
            options: {
              scales: {
                y: {
                  beginAtZero: false // y轴不从0开始
                }
              }
            }
          });
    })
    .catch(error => {
      console.error('Error fetching WTI price:', error);
      document.getElementById('WTIPrice').textContent = 'Unavailable';
    });

}


// 获取每日警句
function fetchDailyQuote(apiKey, fromCurrency, toCurrency) {
    // 定义请求的URL
    const url = 'http://localhost:8000/zhipu/daily_quote';

    // 定义请求头
    const headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    };

    // 定义请求体
    const body = {
      model: 'glm-4'
    };

    // 使用fetch发送POST请求
    fetch(url, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(body)
    })
    .then(response => {
      // 检查响应状态
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      // 解析JSON响应
        return response.json();
    })
    .then(data => {
      // 处理响应数据
      const cleanedText = data.text.replace(/["\n]+/g, '');
      document.getElementById('text').textContent = cleanedText; // 获取数据数组
      console.log('Success:', data);
    })
    .catch(error => {
      // 处理错误
      console.error('Error:', error);
    });

}


// 加载数据指标卡
fetchUsdToCnyRate();
fetchBitcoinPrice();
fetchGoldPrice();
fetchWTIPrice();

//加载每日警句
fetchDailyQuote();