# Pearlhunt: A Python Project for 3D Pearl Hunting

Pearlhunt is a Python-based application designed to simulate the process of hunting for pearls in a 3D space. This project utilizes the Tkinter library for the graphical user interface (GUI), Matplotlib for 3D plotting, and NumPy for numerical operations. The application allows users to either import data from a file or generate random points representing pearls in a 3D space. It then applies an algorithm to determine the most efficient path for collecting these pearls based on their value and distance from the starting point.

## Features

- **3D Plotting**: Utilizes Matplotlib to plot pearls in a 3D space, allowing users to visualize the distribution of pearls.
- **Data Importation**: Users can import data from a file, with each line representing a pearl with its coordinates and value.
- **Random Point Generation**: Generates a specified number of random points within a defined range, each with a random value.
- **Algorithm Execution**: Executes a MOHO (Multi-Objective Optimization Heuristic) algorithm to determine the most efficient path for collecting pearls based on their value and distance.
- **Smart MOHO**: An advanced version of the MOHO algorithm that optimizes the value threshold for maximum pearl collection.
- **Customizable Parameters**: Users can adjust various parameters such as the maximum coordinates, minimum and maximum values for pearls, and the number of pearls to generate or import.

## Installation

To run Pearlhunt, ensure you have Python installed on your system. Then, install the required libraries using pip:

```batch
pip install tkinter matplotlib numpy customtkinter
```

## Usage

1. **Run the Application**: Execute the Python script to launch the Pearlhunt GUI.
2. **Choose Data Source**: Select whether to import data from a file or generate random points.
3. **Configure Parameters**: Adjust the parameters for maximum coordinates, minimum and maximum values for pearls, and the number of pearls to generate or import.
4. **Start Algorithm**: Click the "Start Algorithm" button to run the MOHO algorithm and visualize the most efficient path for collecting pearls.

## Screenshots of the project
![https://github.com/Levy-Y/submarine-algorithm/blob/main/ScreenShots/beta-v1.0-release-screenshot.PNG](Release Screenshot)

## Contributing

Contributions to Pearlhunt are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
