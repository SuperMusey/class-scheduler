import React,{useState} from 'react'
import styles from '../assets/styles/mainpagecontainer.module.css'
import Form from '../components/Form'
import TableContainer from './TableContainer'
import '../utils/__constants__'
//import {fetchData} from '../utils/api'

function MainPageContainer(){
    const [responseData, setResponseData] = useState({
        0:[{ course: '', prof: '', rating: null, start: '', end: '', days: '' },],
    });

    const handleFormSubmit = (formData) => {
        //send fetch req to backend for calculations and get table response
        let data = {
            0: [
                {"course": "Math", "prof": "Dr. Smith", "days": "Mon, Wed"},
                {"course": "Physics", "prof": "Dr. Johnson", "days": "Tue, Thu"},
            ],
            1: [
                {"course": "History", "prof": "Dr. Brown", "days": "Wed, Fri"},
                {"course": "English", "prof": "Dr. Davis", "days": "Mon, Thu"},
            ],
        }
        setResponseData(data)
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