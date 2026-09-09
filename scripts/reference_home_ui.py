from pathlib import Path
import re

p = Path('lib/main.dart')
s = p.read_text(encoding='utf-8')

start = s.find("const Text(\n              'Hızlı kategoriler'")
if start < 0:
    raise SystemExit('reference UI anchor not found')

end = s.find("FutureBuilder<List<Map<String, dynamic>>>(", start)
if end < 0:
    raise SystemExit('campaign list anchor not found')

replacement = r'''Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    const Expanded(
                      child: Text(
                        'Kategoriler',
                        style: TextStyle(fontSize: 20, fontWeight: FontWeight.w900),
                      ),
                    ),
                    TextButton(
                      onPressed: () => setState(() => showAllQuickCategories = !showAllQuickCategories),
                      child: Text(showAllQuickCategories ? 'Daha az' : 'Tümü'),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                GridView.builder(
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  itemCount: showAllQuickCategories ? quick.length : 10,
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 5,
                    crossAxisSpacing: 8,
                    mainAxisSpacing: 8,
                    childAspectRatio: .86,
                  ),
                  itemBuilder: (_, i) {
                    final x = quick[i];
                    final selected = category == x[1];
                    final icon = <String, IconData>{
                      'Akaryakıt': Icons.local_gas_station_rounded,
                      'Otomotiv': Icons.directions_car_rounded,
                      'Market': Icons.shopping_cart_rounded,
                      'Restoran': Icons.restaurant_rounded,
                      'E-ticaret': Icons.shopping_bag_rounded,
                      'Elektronik': Icons.smartphone_rounded,
                      'Giyim': Icons.checkroom_rounded,
                      'Ev & Yaşam': Icons.home_rounded,
                      'Seyahat': Icons.flight_takeoff_rounded,
                      'Eğlence': Icons.movie_rounded,
                    }[x[1]] ?? Icons.category_rounded;

                    return InkWell(
                      borderRadius: BorderRadius.circular(18),
                      onTap: () => setState(() => category = selected ? '' : x[1]),
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 160),
                        padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 9),
                        decoration: BoxDecoration(
                          color: selected
                              ? const Color(0xFF5635E8)
                              : const Color(0xFF101C2F),
                          borderRadius: BorderRadius.circular(18),
                          border: Border.all(
                            color: selected
                                ? const Color(0xFF795BFF)
                                : const Color(0xFF29415F),
                          ),
                        ),
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(
                              icon,
                              size: 28,
                              color: selected
                                  ? Colors.white
                                  : const Color(0xFFB8C7E2),
                            ),
                            const SizedBox(height: 7),
                            Text(
                              x[1],
                              maxLines: 2,
                              overflow: TextOverflow.ellipsis,
                              textAlign: TextAlign.center,
                              style: TextStyle(
                                fontSize: 11,
                                height: 1.05,
                                fontWeight: FontWeight.w800,
                                color: selected
                                    ? Colors.white
                                    : const Color(0xFFD7E0F0),
                              ),
                            ),
                          ],
                        ),
                      ),
                    );
                  },
                ),
                const SizedBox(height: 14),
              ],
            ),

            '''

s = s[:start] + replacement + s[end:]
p.write_text(s, encoding='utf-8')
print('Reference homepage category grid applied')
