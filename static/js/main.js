// navbar script
function toggleOffcanvas() {
    var offcanvas = document.querySelector('.offcanvas');
    var hamoverlay = document.querySelector('.hamoverlay');
    
    // Toggle the display property
    offcanvas.style.display = (offcanvas.style.display === 'flex') ? 'none' : 'flex';
    hamoverlay.style.display = (hamoverlay.style.display === 'block') ? 'none' : 'block';
}

// For Hero Text changing
document.addEventListener('DOMContentLoaded', function () {
  const heroTexts = [
      {
          title: "We Create Investment Worthy Business Plans, Financial Models & Pitch Decks.",
          description: "We have worked with over 150+ clients across Nigeria, Rwanda, UK, Cyprus, India and the US."
          description: "We have worked with over 200+ clients across Nigeria, Rwanda, UK, Cyprus, India and the US."
      },
      {
          title: "We Conduct Primary & Desktop Market Research & Survey for Companies.",
          description: "We have worked with over 150+ clients across Nigeria, Rwanda, UK, Cyprus, India and the US."
          description: "We have worked with over 200+ clients across Nigeria, Rwanda, UK, Cyprus, India and the US."
      },
      {
          title: "We execute the day-to-day activities of a business or organization efficiently and effectively.",
          description: "We have worked with over 150+ clients across Nigeria, Rwanda, UK, Cyprus, India and the US."
          description: "We have worked with over 200+ clients across Nigeria, Rwanda, UK, Cyprus, India and the US."
      },
      {
          title: "We hire and nurture the right talent to help a company achieve its goal and thrive",
          description: "We have worked with over 150+ clients across Nigeria, Rwanda, UK, Cyprus, India and the US."
          description: "We have worked with over 200+ clients across Nigeria, Rwanda, UK, Cyprus, India and the US."
      },
      {
        title: "Emmviron offers expert guidance to help companies make informed decisions, plan for the future, and achieve long-term success",
        description: "Whether you're a new startup, a small business aiming for growth, or a large company seeking innovation, our approach to creating business solutions will help you gain valuable insights and exceed your expectations. Join us on this path to success"
    }
  ];

  const heroh1 = document.querySelector('.heroh1 h1');
  const herop = document.querySelector('.heroh1 p');

  let currentTextIndex = 0;

  function changeText() {
      heroh1.textContent = heroTexts[currentTextIndex].title;
      herop.textContent = heroTexts[currentTextIndex].description;

      currentTextIndex = (currentTextIndex + 1) % heroTexts.length;
  }

  // Initial call
  changeText();

  // Change text every 4 seconds
  setInterval(changeText, 10000);
});


// for Home page Service Cards
document.addEventListener("DOMContentLoaded", function () {
  // Get all the service cards
  var serviceCards = document.querySelectorAll('.each-service-card');

  // Iterate through each service card
  serviceCards.forEach(function (card) {
      // Get SVG, paragraph, and hidden text elements
      var svg = card.querySelector('svg');
      var paragraph = card.querySelector('p');
      var hiddenText = card.querySelector('.hidden-text');

      // Add a mouseover event listener to each card
      card.addEventListener('mouseover', function () {
          // Hide SVG and paragraph
          svg.style.display = 'none';
          paragraph.style.display = 'none';

          // Remove the 'd-none' class to reveal the hidden text
          hiddenText.classList.remove('d-none');
      });

      // Add a mouseout event listener to each card
      card.addEventListener('mouseout', function () {
          // Show SVG and paragraph
          svg.style.display = 'block';
          paragraph.style.display = 'block';

          // Add the 'd-none' class to hide the text again
          hiddenText.classList.add('d-none');
      });
  });
});

function hideClassInIframe() {
    // Get the iframe element
    var iframe = document.getElementById('myIframe');
  
    // Check if the iframe is loaded
    if (iframe) {
      iframe.onload = function() {
        // Access the content of the iframe
        var iframeContent = iframe.contentDocument || iframe.contentWindow.document;
  
        // Hide the elements with the specified class
        var elementsToHide = iframeContent.getElementsByClassName('footerContainer-156e0');
        for (var i = 0; i < elementsToHide.length; i++) {
          elementsToHide[i].style.display = 'none';
        }
      };
    }
  }
  
  // Call the function once the main page is loaded
  window.onload = hideClassInIframe;