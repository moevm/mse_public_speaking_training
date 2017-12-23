  var audio_context;
  var recorder;

  function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
  }

  function upload_voice(){
    var csrftoken = getCookie('csrftoken')
    recorder && recorder.exportWAV(function(blob) {
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/presentation/1/1/upload_voice/', true);
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
      xhr.send(blob);
    });

    recorder.clear();

  }

  function cut_ten_seconds(){
    recorder && recorder.stop();
    upload_voice();
    recorder && recorder.record();
  }


  function startUserMedia(stream) {
    var input = audio_context.createMediaStreamSource(stream);
    console.log('Media stream created.');
    // Uncomment if you want the audio to feedback directly
    //input.connect(audio_context.destination);
    //console.log('Input connected to audio context destination.');

    recorder = new Recorder(input);
    console.log('Recorder initialised.');
  }


  window.onload = function init() {
    try {
      // webkit shim
      window.AudioContext = window.AudioContext || window.webkitAudioContext;
      navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
      window.URL = window.URL || window.webkitURL;

      audio_context = new AudioContext;
      console.log('Audio context set up.');
      console.log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
    } catch (e) {
      alert('No web audio support in this browser!');
    }

    navigator.getUserMedia({audio: true}, startUserMedia, function(e) {
      console.log('No live audio input: ' + e);
    });
  };


  function start_presentation(){
    recorder && recorder.record();
    startTimer();
    setInterval(cut_ten_seconds, 10000);
  }