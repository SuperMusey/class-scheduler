import {BACKEND_URL} from './__constants__'

export const sendData = async (requestData) => {
  const url = BACKEND_URL+'api/data';
  let temp = requestData
  console.log(JSON.stringify(temp))
  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestData),
    });

    const responseData = await response.json();
    return responseData;
  } catch (error) {
    throw new Error('Error:', error);
  }
};