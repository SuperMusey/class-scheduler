import React, { useState } from 'react';
import Table from '../components/Table';
import styles from '../assets/styles/tablecontainer.module.css'

function TableContainer() {
  const [tableDataIndex, setTableDataIndex] = useState(0);

  const tableData = [
    // Place your different table data combinations here
    [
      { course: 'Course 1', prof: 'Professor A', rating: 4.5, start: '2023-08-01', end: '2023-12-15', days: 'Mon-Wed-Fri' },
      { course: 'Course 2', prof: 'Professor B', rating: 3.8, start: '2023-08-15', end: '2023-12-30', days: 'Tue-Thu' },
    ],
    [
      { course: 'Course X', prof: 'Professor Y', rating: 4.2, start: '2023-09-01', end: '2023-12-31', days: 'Mon-Wed' },
      // Add more data combinations as needed
    ],
    // Add more table data combinations as needed
  ];

  const handlePrev = () => {
    setTableDataIndex((prevIndex) => (prevIndex === 0 ? tableData.length - 1 : prevIndex - 1));
  };

  const handleNext = () => {
    setTableDataIndex((prevIndex) => (prevIndex === tableData.length - 1 ? 0 : prevIndex + 1));
  };

  return (
    <div className={styles.table_container}>
      <Table data={tableData[tableDataIndex]} />
      <div className={styles.button_container}>
        <button type='view_tables' onClick={handlePrev}>Prev</button>
        <button type='view_tables' onClick={handleNext}>Next</button>
      </div>
    </div>
  );
}

export default TableContainer;
