const apiKey = 'SBY9nV5Y2EUMWeGJroc8wEySkYQY1xr4FxND80blnRjbwy81mWAlXwuwr8gWqAqC_9FpXBI2s7k5wLCEC1aHgLI3l-Gp1l0A4ODJ3QHqqXO1pd5K5fdarRcC-MaRX3Yx';

const Yelp = {
  search(term, location, sortBy) {
    return fetch(
      `https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?term=${term}&location=${location}&sort_by=${sortBy}`,
        {
          headers: {
            Authorization: `Bearer ${apiKey}`
          }
        }).then((response) => {
        return response.json();
      }).then((jsonResponse) => {
        if (jsonResponse.businesses) {
          return jsonResponse.businesses.map((business) => {
            return {
              id: business.id,
              imageSrc: business.image_url,
              name: business.name,
              address: business.location.address1,
              city: business.location.city,
              state: business.location.state,
              zipCode: business.location.zip_code,
              category: business.categories[0].title,
              rating: business.rating,
              reviewCount: business.review_count
            }
          });
        }
      })
  }
}

export default Yelp;