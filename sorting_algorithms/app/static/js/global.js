document.addEventListener("DOMContentLoaded", () => {
    
    const coll = document.querySelectorAll(".collapsible");

    coll.forEach(button => {
        button.addEventListener("click", function () {
            this.classList.toggle("active");
            const content = this.nextElementSibling;

            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        });
    });

    // Define p5 sketch as a function (instance mode)
    const canvasSketch = (p) => {
        p.arrayStates = []; // array
        p.currentStateIndex = 0;
        
        
        // Canvas construction/positioning on screen
        p.setup = () => {
            const container = document.querySelector("#sketch-container");
            // clientWidth and clientHeight allow canvas border to scale with size
            const c = p.createCanvas(container.clientWidth, container.clientHeight);
            c.parent(container);
        };

        // Canvas Display
        p.draw = () => {
            p.background("black");

            if (p.arrayStates.length > 0) {
                const state = p.arrayStates[p.currentStateIndex];
                p.drawRectangles(state);
                p.currentStateIndex++;
                if (p.currentStateIndex >= p.arrayStates.length) {
                    p.currentStateIndex = p.arrayStates.length - 1; // stop at last state
                }
            }
            
        };

        // instance method to actually draw the rectangles
        p.drawRectangles = (state) => {
            const rectCount = state["array"].length;
            const rectWidth = p.width / rectCount;
            

            for (let index = 0; index < rectCount; index++) {
                const rectHeight = state.array[index];
                // default rectangle color
                p.fill("white");
                p.strokeWeight(0.5);
                // highlight compared indices

                if (state.action === "compare" && (index === state.i)) {
                    p.fill("red"); // highlights the comparison purple
                } else if (state.action === "compare" && (index+1 === state.j)) {
                    p.fill("purple");
                }

                p.rect(
                    index * rectWidth,
                    p.height - rectHeight,
                    rectWidth,
                    rectHeight
                );

            }
        };
        
        // method to load the array states from Flask and place them in array
        p.loadArrayStates = (state) => {
            p.arrayStates = state;
            p.currentStateIndex = 0;
        }
    };

    // Create a new p5 instance
    const sketchInstance = new p5(canvasSketch);

    // Form submission
    const submitBtn = document.querySelector("#inputForm");
    
    submitBtn.addEventListener("submit", async (e) => {
        e.preventDefault();
        const data = await fetchData();
        console.log(data.result);
        sketchInstance.loadArrayStates(data.result);
    });
});

// function to fetch HTML user input for use in Python calculations
async function fetchData() {
    
    const userEntry = document.querySelector("#userEntry");
    const algoType = document.querySelector("#algoType");
    const response = await fetch(`/get_data?userEntry=${userEntry.value}&algoType=${algoType.value}`);

    const jsonData = await response.json();
    return jsonData; // returns a JSON string containing the multiple states of the array during sorting
}
