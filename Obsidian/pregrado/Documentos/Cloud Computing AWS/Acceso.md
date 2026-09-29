# Gestión de Acceso e Identidad: AWS IAM y Modelos de Control de Acceso

La gestión de identidades y accesos (**IAM** - *Identity and Access Management*) es la piedra angular de la seguridad en la nube ([[responsabilidad compartida|Seguridad 'EN' la Nube]]). Controla de forma granular quién está autenticado (autenticación) y qué permisos posee sobre los recursos del sistema (autorización).

---

## 1. Modelos Teóricos de Control de Acceso (ACM)

En la teoría de seguridad informática y control de acceso (**ACM** - *Access Control Models*), existen cuatro paradigmas fundamentales para gobernar las interacciones entre sujetos y objetos:

```
+--------+------------------------------------+-------------------------------------+
| Modelo | Tupla Formal de Control            | Filosofía de Seguridad              |
+--------+------------------------------------+-------------------------------------+
| DAC    | <Sujeto, Acción, Objeto>           | El propietario del objeto decide.   |
| MAC    | <Sujeto, Acción, Nivel/Etiqueta>   | El sistema impone reglas estrictas. |
| RBAC   | <Rol, Acción, Objeto>              | Los permisos dependen del cargo.    |
| ABAC   | <Atributo(S), Atributo(O), Context>| Políticas basadas en atributos.     |
+--------+------------------------------------+-------------------------------------+
```

1. **Control de Acceso Discrecional (DAC - *Discretionary Access Control*)**:
   - **Tupla formal**: $\langle \text{Sujeto}, \text{Acción}, \text{Objeto} \rangle$.
   - **Concepto**: El propietario o creador de un recurso tiene la discreción total de conceder o revocar permisos a otros sujetos.
   - **En AWS**: Se manifiesta tradicionalmente en las Listas de Control de Acceso (**ACLs**) de buckets y objetos en Amazon S3.

2. **Control de Acceso Mandatorio (MAC - *Mandatory Access Control*)**:
   - **Tupla formal**: $\langle \text{Sujeto}, \text{Acción}, \text{Nivel de Seguridad} \rangle$.
   - **Concepto**: Los permisos están determinados centralmente por una autoridad reguladora del sistema mediante niveles de clasificación jerárquicos (Público, Confidencial, Secreto, Alto Secreto) y autorizaciones (*clearances*). Los usuarios no pueden alterar los permisos de sus propios objetos.

3. **Control de Acceso Basado en Roles (RBAC - *Role-Based Access Control*)**:
   - **Tupla formal**: $\langle \text{Rol}, \text{Acción}, \text{Objeto} \rangle$.
   - **Concepto**: Los permisos se asocian a roles funcionales abstractos dentro de una organización (por ejemplo: `DevOpsEngineer`, `AuditorFinanciero`), y los sujetos humanos o procesos adquieren permisos al ser asignados a uno o varios roles.
   - **En AWS**: Se implementa a través de los **Grupos de Usuarios IAM** y los **Roles IAM**.

4. **Control de Acceso Basado en Atributos (ABAC - *Attribute-Based Access Control*)**:
   - **Tupla formal**: $\langle \text{Atributos del Sujeto}, \text{Atributos del Objeto}, \text{Atributos del Entorno} \rangle$.
   - **Concepto**: Evalúa etiquetas (*tags*), condiciones de red, horario y variables contextuales en tiempo real para autorizar una solicitud.
   - **En AWS**: Se implementa en las políticas IAM mediante etiquetas (`aws:PrincipalTag/Department = aws:ResourceTag/Department`) y el bloque `Condition`.

---

## 2. Identidades en AWS IAM

AWS IAM permite modelar las identidades operativas de personas y sistemas dentro de una cuenta:

```mermaid
graph TD
    IAM["Entidades de AWS IAM"] --> Root["1. Usuario Raíz (Root User)"]
    IAM --> Users["2. Usuarios IAM (Humanos/Sistemas)"]
    IAM --> Groups["3. Grupos de Usuarios (Colección lógica)"]
    IAM --> Roles["4. Roles IAM (Identidad sin credenciales fijas)"]
    
    Roles --> EC2Role["Instance Profiles (EC2 / Servicios)"]
    Roles --> Fed["Federación de Identidades (OIDC / SAML 2.0)"]
```

### 2.1. Usuario Raíz (*Root User*)
- Es la identidad creada al momento de abrir la cuenta de AWS, identificada mediante la dirección de correo electrónico del propietario.
- Posee **acceso total, absoluto e irrestricto** a todos los recursos y configuraciones de facturación. No puede ser limitado por ninguna política IAM regular dentro de la cuenta.
- **Mejores prácticas de securización obligatorias**:
  1. Habilitar inmediatamente **Autenticación Multifactorial (MFA)** física (llave de seguridad FIDO U2F) o virtual (TOTP).
  2. **Eliminar permanentemente las claves de acceso de API** (*Access Keys*) asociadas al usuario raíz.
  3. No utilizar nunca el usuario raíz para tareas administrativas cotidianas; crear en su lugar un usuario administrador IAM o configurar acceso federado vía **AWS IAM Identity Center**.

### 2.2. Usuarios IAM (*IAM Users*)
- Entidades que representan a una persona o aplicación individual que interactúa con AWS.
- Tienen credenciales permanentes a largo plazo (contraseña de consola y/o hasta 2 pares de claves de acceso de API).

### 2.3. Grupos de Usuarios IAM (*IAM User Groups*)
- Colecciones lógicas de usuarios IAM diseñadas para facilitar la asignación masiva de políticas de permisos.
- **Regla técnica**: Los grupos no pueden contener a otros grupos (no se permite el anidamiento jerárquico de grupos). Un usuario puede pertenecer a múltiples grupos simultáneamente.

### 2.4. Roles IAM (*IAM Roles*)
- Identidades seguras que **no poseen contraseñas ni claves de acceso a largo plazo**. En su lugar, proporcionan **credenciales temporales de seguridad** de corta duración generadas por **AWS STS** (*Security Token Service*).
- **Casos de uso críticos**:
  - **Servicios de AWS**: Por ejemplo, asignar un rol a una instancia EC2 a través de un perfil de instancia (*Instance Profile*) para que el software dentro de la máquina acceda a un bucket de S3 sin almacenar claves de API en archivos de texto plano.
  - **Federación de Identidades Corporativas**: Integración mediante estándares **SAML 2.0** u **OpenID Connect (OIDC)** con proveedores de identidad externos (Google Workspace, Microsoft Entra ID, Okta, GitHub Actions para CI/CD).
  - **Acceso entre Cuentas (*Cross-Account Access*)**: Permitir que identidades de la Cuenta A asuman temporalmente un rol en la Cuenta B.

---

## 3. Estructura y Sintaxis de las Políticas IAM (Documento JSON)

Una política IAM es un documento estructurado en formato **JSON** que define formalmente los permisos de autorización:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadSpecificPrefix",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::empresa-datos-produccion",
        "arn:aws:s3:::empresa-datos-produccion/*"
      ],
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "190.14.23.0/24"
        },
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    }
  ]
}
```

### Desglose Semántico de Elementos:

- **`Version`**: Especifica la versión del lenguaje de políticas. El estándar actual siempre debe ser `"2012-10-17"`.
- **`Statement`**: Arreglo principal que contiene una o más declaraciones individuales de permisos.
  - **`Sid` (*Statement ID*)**: Identificador alfanumérico opcional para describir el propósito de la declaración.
  - **`Effect`**: Determina el resultado de la regla. Valores permitidos estrictamente: `"Allow"` o `"Deny"`.
  - **`Principal`**: Especifica la identidad (usuario, rol, cuenta o servicio) a la que se aplica la política. **Solo es obligatorio en políticas basadas en recursos** (como las políticas de buckets S3) y en políticas de confianza de roles (*Trust Policies*). En políticas basadas en identidad, el sujeto que porta la política es el principal implícito.
  - **`Action`**: Lista de llamadas a la API de AWS que se permiten o deniegan (por ejemplo: `"s3:GetObject"`, `"ec2:RunInstances"`, `"rds:CreateDBInstance"`).
  - **`Resource`**: Uno o varios nombres de recursos de Amazon (**ARN** - *Amazon Resource Name*) sobre los cuales se ejecuta la acción (ej: `arn:aws:s3:::mi-bucket/*`).
  - **`Condition`**: Bloque opcional que evalúa expresiones lógicas booleanas, operadores de cadenas, rangos de IP o atributos contextuales en tiempo real para autorizar la solicitud.

---

## 4. Tipos de Políticas en AWS

1. **Políticas Basadas en Identidad (*Identity-Based Policies*)**: Se adjuntan directamente a usuarios, grupos o roles IAM.
   - *Gestionadas por AWS (AWS Managed)*: Creadas y administradas por AWS.
   - *Gestionadas por el Cliente (Customer Managed)*: Creadas por los administradores de la cuenta.
   - *En línea (Inline)*: Incrustadas directamente en una sola identidad.
2. **Políticas Basadas en Recursos (*Resource-Based Policies*)**: Se adjuntan directamente al recurso de destino (ejemplo: S3 Bucket Policies, KMS Key Policies, políticas de colas SQS).
3. **Límites de Permisos (*Permissions Boundaries*)**: Característica avanzada que define los permisos máximos que una política basada en identidad puede otorgar a un usuario o rol, impidiendo la escalación de privilegios.
4. **Políticas de Control de Servicios (*Service Control Policies - SCP*)**: Reglas de gobernanza centralizadas aplicadas a nivel de Unidad Organizacional (OU) o cuenta mediante **AWS Organizations** que establecen los permisos máximos absolutos para todas las identidades de esa cuenta.

---

## 5. Algoritmo y Flujo de Evaluación de Políticas IAM

Cuando una identidad intenta invocar una API en AWS, el motor de autorización ejecuta un algoritmo determinista estricto:

```mermaid
flowchart TD
    Inicio([Solicitud de API entrante]) --> DefaultDeny[1. Denegación Implícita Inicial]
    DefaultDeny --> SCPCheck{¿Permitido por SCP en Organizations?}
    SCPCheck -- No --> DenyOut([Acceso DENEGADO])
    SCPCheck -- Sí --> ExplicitDenyCheck{¿Existe un DENY explícito en alguna política?}
    ExplicitDenyCheck -- Sí --> DenyOut
    ExplicitDenyCheck -- No --> PermBoundaryCheck{¿Permitido por Permissions Boundary si aplica?}
    PermBoundaryCheck -- No --> DenyOut
    PermBoundaryCheck -- Sí --> ExplicitAllowCheck{¿Existe al menos un ALLOW explícito?}
    ExplicitAllowCheck -- Sí --> AllowOut([Acceso PERMITIDO])
    ExplicitAllowCheck -- No --> DenyOut
```

> [!important] Las Tres Leyes de la Evaluación de IAM
> 1. **Denegación por Omisión (*Default Deny*)**: Por defecto, cualquier solicitud está denegada a menos que exista una regla explícita que la permita.
> 2. **Permisión Explícita (*Explicit Allow*)**: Se requiere al menos un `Allow` explícito en una política aplicable para autorizar la acción.
> 3. **Denegación Explícita Absoluta (*Explicit Deny*)**: **Cualquier regla de `Deny` explícito prevalece y anula inmediatamente cualquier regla de `Allow`**, sin importar el tipo de política en la que se encuentre.

---

## 6. Métodos de Acceso y Credenciales

| Canal de Acceso | Mecanismo de Autenticación | Tipo de Credencial | Caso de Uso |
| :--- | :--- | :--- | :--- |
| **Consola de Administración de AWS** | Nombre de usuario / Contraseña + MFA. | Credencial interactiva humana con sesión web caducable. | Gestión visual, auditoría manual, monitoreo. |
| **AWS CLI / AWS SDK** | `Access Key ID` (ej. `AKIAIOSFODNN7EXAMPLE`) y `Secret Access Key`. | Credenciales criptográficas de larga duración. | Automatización local, scripts administrativos. *(Desaconsejado para servidores internos)*. |
| **AWS STS (Security Token Service)** | `AccessKeyId`, `SecretAccessKey` y `SessionToken`. | **Credenciales temporales de corta duración** (15 min a 36 h). | Asunción de Roles IAM por instancias EC2, Lambdas, CI/CD y federación externa. |

---

## Notas relacionadas
- [[Cloud computing]] - Fundamentos de seguridad, gobernanza y Well-Architected Framework.
- [[responsabilidad compartida]] - Configuración de IAM y protección de claves como responsabilidad del cliente.
- [[vpc]] - Políticas de endpoint (VPC Endpoints) y control de acceso a nivel de red.
- [[ebs(network)]] - Políticas IAM para la gestión de volúmenes, snapshots y llaves KMS asociadas.
- [[EFS elastic file system]] - Autorización de montaje y permisos de acceso para clientes NFS.
- [[tipos de soporte aws]] - Delegación de roles y permisos para soporte técnico de AWS.
- [[sgsi]] - Sistema de Gestión de Seguridad de la Información (ISO/IEC 27001).
- [[egsi]] - Esquema de Gobernanza y Seguridad de la Información.
- [[linea base]] - Líneas base de configuración segura de identidades y accesos.
