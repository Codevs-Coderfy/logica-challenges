function generarTabla() {
      let numero = parseInt(document.getElementById("numero").value);
      let salida = "";

      // Bucle con if
      for (let i = 1; i <= 10; i++) {
        let resultado = numero * i;

        if (resultado > 50) {
          salida += `${numero} x ${i} = ${resultado} → resultado mayor a 50\n`;
        } else {
          salida += `${numero} x ${i} = ${resultado}\n`;
        }
      }

      // Mostrar en el campo de salida
      document.getElementById("output").textContent = salida;
    }