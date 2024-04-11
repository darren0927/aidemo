document.addEventListener('DOMContentLoaded', function() {
  // 准备数据，这里使用静态数据作为示例
  const words = [
    {text: 'JavaScript', weight: 10},
    {text: 'D3', weight: 8},
    {text: 'Chrome', weight: 6},
    {text: 'Extension', weight: 7},
    // 添加更多的单词和权重...
  ];

  // 设置词云的布局
  const layout = d3.layout.cloud()
    .size([300, 300])
    .words(words.map(function(d) {
      return {text: d.text, size: d.weight * 10};
    }))
    .padding(5)
    .rotate(function() { return ~~(Math.random() * 2) * 90; })
    .font('Impact')
    .fontSize(function(d) { return d.size; })
    .on('end', draw);

  layout.start();

  function draw(words) {
    // 使用Voronoi Stippling
    const voronoiStippling = new VoronoiStippling({ width: 300, height: 300 });

    d3.select('#word-cloud').append('svg')
      .attr('width', layout.size()[0])
      .attr('height', layout.size()[1])
      .append('g')
        .attr('transform', 'translate(' + layout.size()[0] / 2 + ',' + layout.size()[1] / 2 + ')')
      .selectAll('text')
        .data(words)
      .enter().append('text')
        .style('font-size', function(d) { return d.size + 'px'; })
        .style('font-family', 'Impact')
        .attr('text-anchor', 'middle')
        .attr('transform', function(d) {
          return 'translate(' + [d.x, d.y] + ')';
        })
        .text(function(d) { return d.text; });

    // 你需要进行voronoi-stippling库特定的操作来完成词云的风格设定
    // 请参考库的文档以了解如何使用它来实现所需的效果
  }
});
