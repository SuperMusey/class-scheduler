
const fetchData = async (url, params) => {
  try {
    // Construct the query string from the JSON parameters
    const queryParams = new URLSearchParams(params);

    // Construct the complete URL with query parameters
    const completeUrl = url + '?' + queryParams.toString();

    // Perform the GET request using fetch
    const response = await fetch(completeUrl, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        // Add any other headers if needed
      },
    });

    // Parse the JSON response
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};


export default fetchData;
