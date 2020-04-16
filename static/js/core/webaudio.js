/*
    Theme Name: i-CityAssistant
    Author: Alcindo Schleder
    Author URL: https://icity.net.br
*/
const WebAudio = function() {
    var audioChunks = null;
    var mediaRecorder = null;
    var stopped = true;
    var mediaUrl = null;
    var audioMedia = null;
    var has_audio = false;
    var constraints = {
        audio: true,
        video: false
    }

    const InitAudioDevice = function() {
        navigator.getUserMedia(constraints, startAudioDevice, function(err) {
            has_audio = false;
            console.log('Error on start audio device!', err);
            alert('Error on start audio device! ', err.message);
        });
    };
    const initVaribles= function () {
        audioChunks = [];
        mediaUrl = null;
        audioMedia = null;
    };
    const startAudioDevice = function (stream) {
        has_audio = true;
        stopped = true;
        const options = {mimeType: 'video/webm;codecs=vp9'};
        mediaRecorder = new MediaRecorder(stream, options);
        mediaRecorder.addEventListener("dataavailable", e => {
            if (e.data.size > 0)
                audioChunks.push(e.data);
        });
    };
    const startAudioRecord = function () {
        initVaribles();
        if (has_audio) {
            stopped = false;
            mediaRecorder.start();
        }
    };
    const stopAudioRecord = function () {
        if ((has_audio) && (!stopped)) {
            return new Promise(resolve => {
                mediaRecorder.onstop =  async () => {
                    await setAudioBuffer()
                    mediaRecorder.on
                    return resolve();
                };
                mediaRecorder.stop();
            });

        }
    };
    const setAudioBuffer = async function() {
        if (has_audio) {
            stopped = true;
            const audioBlob = new Blob(audioChunks);
            mediaUrl = window.URL.createObjectURL(audioBlob);
            audioMedia = new Audio(mediaUrl);
            mediaRecorder.onstop = null;
        }
    };
    const getAudio = function() {
        return ((has_audio) && (audioMedia)) ? audioMedia : null;
    }
    const getAudioUrl = function() {
        return (has_audio) ? mediaUrl : null;
    };
    return {
        //main function to initiate the module
        Init: function () {
            InitAudioDevice();
        },
        startRecord: function () {
            startAudioRecord();
        },
        stopRecord: async function () {
            await stopAudioRecord();
        },
        audioData: function () {
            return getAudio();
        },
        playAudio: function () {
            audio = getAudio();
            if (audio)
                audio.play();
        },
        audioUrl: function () {
            return getAudioUrl();
        },
        checkRecord: function () {
            return stopped;
        }
    };

} ();

$(document).ready(() => {
    //normalize window.AudioContext
    window.AudioContext || (window.AudioContext = window.AudioContext || window.webkitAudioContext);
    //normalize navigator.getUserMedia
    navigator.getUserMedia || (navigator.getUserMedia = navigator.webkitGetUserMedia ||
                               navigator.mozGetUserMedia || navigator.msGetUserMedia);
    setTimeout(() => {
        WebAudio.Init();
     }, 1000);
