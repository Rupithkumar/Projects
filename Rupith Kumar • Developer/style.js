document.getElementById('toggleTheme').addEventListener('click', function() {
    document.body.classList.toggle('dark');
    const sun = document.querySelector('#toggleTheme .sun');
    const moon = document.querySelector('#toggleTheme .moon');
    if (document.body.classList.contains('dark')) {
        sun.style.opacity = '0';
        moon.style.opacity = '1';
    } else {
        sun.style.opacity = '1';
        moon.style.opacity = '0';
    }
});
document.addEventListener('mousemove', function(event) {
    const customCursor = document.getElementById('customCursor');
    customCursor.style.left = `${event.pageX}px`;
    customCursor.style.top = `${event.pageY}px`;
});
document.querySelectorAll('a, button, input[type="button"], input[type="submit"], .hoverable-div').forEach(el => {
    el.addEventListener('mouseenter', function() {
        document.getElementById('customCursor').classList.add('hidden');
    });
    el.addEventListener('mouseleave', function() {
        document.getElementById('customCursor').classList.remove('hidden');
    });
});
let isScrolling;
document.addEventListener('scroll', function() {
    const customCursor = document.getElementById('customCursor');
    customCursor.style.height = '80px'; 
    window.clearTimeout(isScrolling);
    isScrolling = setTimeout(function() {
        customCursor.style.height = '20px'; 
    }, 150);
});
let circularProgress = document.querySelector(".circular-progress");
let progressValue = document.querySelector(".progress-value");
let progressStartValue = 0;
let progressEndValue = 70;
let speed = 100;

let progress = setInterval(() => {
    progressStartValue++;
    progressValue.textContent = `${progressStartValue}%`;
    circularProgress.style.background = `conic-gradient(#7d2ae8 ${progressStartValue * 3.6}deg, #ededed 0deg)`;

    if (progressStartValue === progressEndValue) {
        clearInterval(progress);
    }
}, speed);
let circularProgress1 = document.querySelector(".circular-progress1");
let progressValue1 = document.querySelector(".progress-value1");
let progressStartValue1 = 0;
let progressEndValue1 = 75;

let progress1 = setInterval(() => {
    progressStartValue1++;
    progressValue1.textContent = `${progressStartValue1}%`;
    circularProgress1.style.background = `conic-gradient(#29de23 ${progressStartValue1*3.6}deg, #ededed 0)`;

    if (progressStartValue1 === progressEndValue1) {
        clearInterval(progress1);
    }
}, speed);
let circularProgress2 = document.querySelector(".circular-progress2");
let progressValue2 = document.querySelector(".progress-value2");
let progressStartValue2 = 0;
let progressEndValue2 = 90;


let progress2 = setInterval(() => {
    progressStartValue2++;
    progressValue2.textContent = `${progressStartValue2}%`;
    circularProgress2.style.background = `conic-gradient(#e8302a ${progressStartValue2*3.6}deg, #ededed 0)`;

    if (progressStartValue2 === progressEndValue2) {
        clearInterval(progress2);
    }
}, speed);
//
let circularProgress3 = document.querySelector(".circular-progress3");
let progressValue3 = document.querySelector(".progress-value3");
let progressStartValue3 = 0;
let progressEndValue3 = 83;


let progress3 = setInterval(() => {
    progressStartValue3++;
    progressValue3.textContent = `${progressStartValue3}%`;
    circularProgress3.style.background = `conic-gradient(#fe29db ${progressStartValue3*3.6}deg, #ededed 0)`;

    if (progressStartValue3 === progressEndValue3) {
        clearInterval(progress3);
    }
}, speed);
//
let circularProgress4 = document.querySelector(".circular-progress4");
let progressValue4 = document.querySelector(".progress-value4");
let progressStartValue4 = 0;
let progressEndValue4 = 70;


let progress4 = setInterval(() => {
    progressStartValue4++;
    progressValue4.textContent = `${progressStartValue4}%`;
    circularProgress4.style.background = `conic-gradient(#2ae8b9 ${progressStartValue4*3.6}deg, #ededed 0)`;

    if (progressStartValue4 === progressEndValue4) {
        clearInterval(progress4);
    }
}, speed);
let circularProgress5 = document.querySelector(".circular-progress5");
let progressValue5 = document.querySelector(".progress-value5");
let progressStartValue5 = 0;
let progressEndValue5 = 50;


let progress5 = setInterval(() => {
    progressStartValue5++;
    progressValue5.textContent = `${progressStartValue5}%`;
    circularProgress5.style.background = `conic-gradient(#2a56e8 ${progressStartValue5*3.6}deg, #ededed 0)`;

    if (progressStartValue5 === progressEndValue5) {
        clearInterval(progress5);
    }
}, speed);
document.getElementById('close').addEventListener('click', function() {
    const message = document.getElementById('message1');
    message.style.opacity = '0'; 
    setTimeout(() => {
        message.style.display = 'none'; 
    }, 500); 
});

function showMessage() {
    const message = document.getElementById('message1');
    message.style.display = 'block'; 
    setTimeout(() => {
        message.style.opacity = '1'; 
    }, 10); 
}

document.getElementById('show').addEventListener('click', function(event) {
    event.preventDefault();
    showMessage();
});

document.getElementById('showmess').addEventListener('click', function(event) {
    event.preventDefault();
    showMessage();
});