import React from 'react'
import styles from '../assets/styles/mainpagecontainer.module.css'
import Form from '../components/Form'
import TableContainer from './TableContainer'
import '../utils/__constants__'

function MainPageContainer(){
    return(
        <div className={styles.body_container}>
            <Form/>
            <TableContainer/>
        </div>
    );
}

export default MainPageContainer