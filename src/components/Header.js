// Header.js
import React from 'react';
import styles from '../assets/styles/header.module.css'
import logo from'../assets/images/bulogo.png'

function Header(){
  return (
    <header className={styles.header}>  
      <img src={logo} alt='logo'/>
      <h1>Boston University Course Scheduling Tool</h1>
    </header>
  );
};

export default Header;
