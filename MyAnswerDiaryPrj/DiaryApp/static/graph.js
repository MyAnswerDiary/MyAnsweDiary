const chart1 = document.querySelector('.doughnut1');
const chart2 = document.querySelector('.doughnut2');
const chart3 = document.querySelector('.doughnut3');
const chart4 = document.querySelector('.doughnut4');

const makeChart = (percent, classname, color) => {
  let i = 1;
  let chartFn = setInterval(function() {
    if (i < percent) {
      colorFn(i, classname, color);
      i++;
    } else {
      clearInterval(chartFn);
    }
  }, 10);
}

const colorFn = (i, classname, color) => {
  classname.style.background = "conic-gradient(" + color + " 0% " + i + "%, #dedede " + i + "% 100%)";
}

const replay = () => {
  makeChart(45, chart1, '#F6C8AE');
  makeChart(35, chart2, '#EF9E85');
  makeChart(15, chart3, '#5A7E64');
  makeChart(5, chart4, '#A3B899');
}

makeChart(45, chart1, '#F6C8AE');
makeChart(35, chart2, '#EF9E85');
makeChart(15, chart3, '#5A7E64');
makeChart(5, chart4, '#A3B899');