-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-07-2023 a las 06:49:01
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `yuri`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuenta`
--

CREATE TABLE `cuenta` (
  `Usuario_ID` int(11) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Clave_Usuario` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `D_ID` int(11) NOT NULL,
  `D_codigo` int(11) NOT NULL,
  `Nom_departamento` varchar(25) NOT NULL,
  `Cargo` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajador`
--

CREATE TABLE `trabajador` (
  `T_ID` int(11) NOT NULL,
  `T_RUT` varchar(11) NOT NULL,
  `T_Nombre` varchar(20) NOT NULL,
  `T_Sexo` varchar(10) NOT NULL,
  `T_Direccion` varchar(15) NOT NULL,
  `T_Telefono` varchar(15) NOT NULL,
  `T_FechaIngreso` varchar(12) NOT NULL,
  `Usuario_ID` int(11) NOT NULL,
  `T_F_ID` int(11) NOT NULL,
  `T_E_ID` int(11) NOT NULL,
  `D_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `t_cargas_familiares`
--

CREATE TABLE `t_cargas_familiares` (
  `T_F_ID` int(11) NOT NULL,
  `T_F_Rut` int(11) NOT NULL,
  `T_F_Nombre` varchar(30) NOT NULL,
  `T_F_Edad` int(11) NOT NULL,
  `T_F_Parentesco` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `t_contactos_emergencia`
--

CREATE TABLE `t_contactos_emergencia` (
  `T_E_ID` int(11) NOT NULL,
  `T_E_Rut` int(11) NOT NULL,
  `T_E_Nombre` varchar(30) NOT NULL,
  `T_E_Numero` int(11) NOT NULL,
  `T_E_Relacion` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cuenta`
--
ALTER TABLE `cuenta`
  ADD PRIMARY KEY (`Usuario_ID`);

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`D_ID`);

--
-- Indices de la tabla `trabajador`
--
ALTER TABLE `trabajador`
  ADD PRIMARY KEY (`T_ID`),
  ADD KEY `Usuario_ID` (`Usuario_ID`),
  ADD KEY `T_F_ID` (`T_F_ID`),
  ADD KEY `T_E_ID` (`T_E_ID`),
  ADD KEY `D_ID` (`D_ID`);

--
-- Indices de la tabla `t_cargas_familiares`
--
ALTER TABLE `t_cargas_familiares`
  ADD PRIMARY KEY (`T_F_ID`);

--
-- Indices de la tabla `t_contactos_emergencia`
--
ALTER TABLE `t_contactos_emergencia`
  ADD PRIMARY KEY (`T_E_ID`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `trabajador`
--
ALTER TABLE `trabajador`
  ADD CONSTRAINT `trabajador_ibfk_1` FOREIGN KEY (`Usuario_ID`) REFERENCES `cuenta` (`Usuario_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `trabajador_ibfk_2` FOREIGN KEY (`T_F_ID`) REFERENCES `t_cargas_familiares` (`T_F_ID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `trabajador_ibfk_3` FOREIGN KEY (`T_E_ID`) REFERENCES `t_contactos_emergencia` (`T_E_ID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `trabajador_ibfk_4` FOREIGN KEY (`D_ID`) REFERENCES `departamento` (`D_ID`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
