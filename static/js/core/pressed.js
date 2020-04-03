const Pressed = function () {
    let element = null;
    let timerID = null;
    let pressHoldEvent = null;
    let counter = 0;
    const pressHoldDuration = 20;

    const initEvents = function(elDom) {
        element = elDom;
        pressHoldEvent = new CustomEvent("pressHold");
        buttomPressed();
    }
    const pressingDown = function (e) {
        // Start the timer
        requestAnimationFrame(timer);
        e.preventDefault();

    };
    
    const notPressingDown = function (e) {
        // Stop the timer
        cancelAnimationFrame(timerID);
        counter = 0;
        element.dispatchEvent(pressHoldEvent);
    };
    const timer = function () {
        if (counter < pressHoldDuration) {
            timerID = requestAnimationFrame(timer);
            counter++;        
        } else {
            element.dispatchEvent(pressHoldEvent);
        }
    };
    const doSomething = async function (e) {
        // Open Microphone and save into file for send to Watson Assistant
        if ((WebAudio === undefined) || (WebAudio.checkRecord() === undefined))
            return false
        if (WebAudio.checkRecord())
            WebAudio.startRecord();
        else {
            await WebAudio.stopRecord();
            WebAudio.playAudio();
        }
    };
    const buttomPressed = function () {    
        // Listening for the mouse and touch events    
        element.addEventListener("mousedown", pressingDown, false);
        element.addEventListener("mouseup", notPressingDown, false);
        // element.addEventListener("mouseleave", notPressingDown, false);
    
        element.addEventListener("touchstart", pressingDown, false);
        element.addEventListener("touchend", notPressingDown, false);
    
        // Listening for our custom pressHold event
        element.addEventListener("pressHold", doSomething, false);
    };
    return {
        Init: function (elDom) {
            initEvents(elDom)
        }
    };
}();
