import React,{useState} from 'react'
import styles from '../assets/styles/mainpagecontainer.module.css'
import Form from '../components/Form'
import TableContainer from './TableContainer'
import '../utils/__constants__'
import {sendData} from '../utils/api'
import {getCoursesInputedAsArray} from '../utils/parsing'

function MainPageContainer(){
    const [responseData, setResponseData] = useState({
        0:[{ course: '', prof: '', rating: null, start: '', end: '', days: '' },],
    });

    const handleFormSubmit = async (formData) => {
        try {
          // Send fetch req to backend for calculations and get table response
          const response = await sendData(getCoursesInputedAsArray(formData));
          console.log(response)
          setResponseData({
            0:[{ course: '', prof: '', rating: null, start: '', end: '', days: '' },],
        }); // Update the state with the parsed response data
        } catch (error) {
          console.error('Error:', error);
        }
      };

    return(
        <div className={styles.body_container}>
            <div className={styles.form_div}>
                <Form onFormSubmit={handleFormSubmit}/>
            </div>
            <TableContainer responseDataTable={responseData}/>
        </div>
    );
}

export default MainPageContainer