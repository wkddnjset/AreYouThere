$(document).ready(function() {
  $('#calendar').fullCalendar({
    header: {
      left:'',
      center: 'prev, title, next',
      right:'',
    },
    height: 600,
    titleFormat:'YYYY.M',
    defaultDate: m.format("YYYY-MM-DD"),
    navLinks: false, // can click day/week names to navigate views
    editable: false,
    eventLimit: true, // allow "more" link when too many events
    events: [
      {
        title: '8.5',
        start: '2018-06-01'
      },
      {
        title: '8.5',
        start: '2018-06-07',
      },
      {
        title: '5.5',
        start: '2018-06-13'
      },
      {
        title: '6.5',
        start: '2018-06-14'
      },
      {
        title: '4.5',
        start: '2018-06-25',
      },
      {
        title: '0.5',
        start: '2018-06-27',
      },
  
    ]
  });

});