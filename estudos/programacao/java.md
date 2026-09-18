---
titulo: "java"
categoria: "Programação"
nivel: "Iniciante"
atualizado_em: "2026-08-28T17:14:00.000Z"
---

# java




























```java
package exercicios;
import java.util.Scanner;

public class um {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.err.println("Digite um numero: ");
        int numero = scanner.nextInt();

        if (numero % 2 == 0){
            System.out.println("Esse numero é Par");
        }
        else { System.out.println("Esse numero é Impar");    
        }
                scanner.close();
        }
}

```


