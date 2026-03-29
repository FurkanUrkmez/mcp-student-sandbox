# mystery_module

## Proje Başlığı
mystery_module – Quadratic Equation Solver

## Açıklama
`mystery_module` kısa, tek sorumluluklu bir Python modülüdür. Verilen katsayılarla ikinci dereceden denklemin köklerini çözer. Negatif diskriminant durumunda `None` döner (gerçek kök yok).

## Fonksiyonlar
- `fn_x(a, b, c)`
  - Hesaplama: `d = b**2 - 4*a*c`
  - `d < 0`: `None` (gerçek kök yok)
  - `d >= 0`: iki gerçek kök `(x1, x2)` döner
  - `a`, `b`, `c`: ikinci, birinci ve sabit terim katsayıları

## Kurulum
1. Python 3.6+ kurun.
2. Depoyu klonlayın:
   ```bash
   git clone <repo-url>
   cd mcp-student-sandbox
   ```
3. Gerekiyorsa sanal ortam oluşturun:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   ```

## Kullanım
```python
from mystery_module import fn_x

result = fn_x(1, -3, 2)
print(result)  # (2.0, 1.0)

result = fn_x(1, 0, 1)
print(result)  # None
```

## Örnekler
- `fn_x(1, 5, 6)` -> `(-2.0, -3.0)`
- `fn_x(1, 0, -4)` -> `(2.0, -2.0)`
- `fn_x(1, 0, 1)` -> `None`

## Hata durumları
- `a == 0`: Bu durumda modül bu lineer durumun kontrolünü yapmaz; TypeError veya ZeroDivisionError oluşabilir.
- `a`, `b`, `c` numeric değilse TypeError oluşabilir.

## Geliştirme Tavsiyeleri
- `d < 0` için karmaşık kökleri destekleyecek şekilde genişletin.
- `a == 0` kontrolü ekleyip `ValueError` fırlatın.
- Birim testleri ekleyin (`pytest`).
- Güvenlik ve kod kalite kontrolü için `flake8`/`pylint` ekleyin.
 