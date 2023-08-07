import React, { useState } from 'react';
import Table from '../components/Table';
import styles from '../assets/styles/tablecontainer.module.css'

function TableContainer({responseDataTable}) {

  const [tableDataIndex, setTableDataIndex] = useState(0);
  
  const handlePrev = () => {
    setTableDataIndex((prevIndex) => (prevIndex === 0 ? Object.keys(responseDataTable).length - 1 : prevIndex - 1));
  };

  const handleNext = () => {
    setTableDataIndex((prevIndex) => (prevIndex === Object.keys(responseDataTable).length - 1 ? 0 : prevIndex + 1));
  };

  return (
    <div className={styles.table_container}>
      <Table data={responseDataTable[tableDataIndex]} />
      <div className={styles.button_container}>
        <button type='view_tables' onClick={handlePrev}>Prev</button>
        <button type='view_tables' onClick={handleNext}>Next</button>
      </div>
    </div>
  );
}

export default TableContainer;
