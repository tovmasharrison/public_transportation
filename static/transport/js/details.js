// Get the container for the star rating
const starRatingContainer = document.querySelector('.star-rating');

// Calculate the star rating
const avgRate = parseFloat('{{ avg_rate }}');
const starRatingPercentage = (avgRate / 5) * 100;

// Set the width of the star rating container
starRatingContainer.style.width = `${starRatingPercentage}%`;
