document.addEventListener('DOMContentLoaded', () => {

    const slider = document.querySelector('.slider');

    if (!slider) return;

    const nextBtn = document.querySelector('.next');
    const prevBtn = document.querySelector('.prev');

    nextBtn.addEventListener('click', () => {
        slider.scrollBy({
            left: 300,
            behavior: 'smooth'
        });
    });

    prevBtn.addEventListener('click', () => {
        slider.scrollBy({
            left: -300,
            behavior: 'smooth'
        });
    });

    setInterval(() => {
        slider.scrollBy({
            left: 300,
            behavior: 'smooth'
        });

        if (
            slider.scrollLeft + slider.clientWidth >=
            slider.scrollWidth - 10
        ) {
            slider.scrollTo({
                left: 0,
                behavior: 'smooth'
            });
        }

    }, 4000);

});