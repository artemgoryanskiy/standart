const counters = document.querySelectorAll('.count');
const speed = 200;

counters.forEach((counter) => {
    const updateCount = () => {
        const target = parseInt(+counter.getAttribute('data-target'));
        const count = parseInt(+counter.innerText);
        let increment = 0;

        if (target < speed) {
            increment = 1;
        } else
            increment = Math.trunc(target / speed);

        if (count < target) {
            counter.innerText = count + increment;
            setTimeout(updateCount, 1);
        } else {
            counter.innerText = target;
        }
    };
    updateCount();
});