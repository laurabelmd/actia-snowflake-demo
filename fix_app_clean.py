#!/usr/bin/env python3
"""
Script to fix all indentation errors in app.py
"""

with open('app.py', 'r') as f:
    lines = f.readlines()

# Corrections needed based on context
corrections = []
fixed_lines = []

i = 0
while i < len(lines):
    line = lines[i]
    
    # Check if we're inside a 'with tabs[1]:' block for defect detection
    # Lines inside should have proper indentation
    
    # Pattern 1: st.markdown after '# Simuler un cercle rouge' should be indented 20 spaces (5 levels)
    if i > 0 and '# Simuler' in lines[i-1] and line.strip().startswith('st.markdown'):
        # Should be 20 spaces (inside if button click, which is inside with col, which is inside if uploaded, which is inside with tabs[1], which is inside elif page)
        if not line.startswith('                    '):  # 20 spaces
            fixed_line = '                    ' + line.lstrip()
            fixed_lines.append(fixed_line)
            corrections.append(f"Line {i+1}: Fixed indentation for st.markdown after comment")
        else:
            fixed_lines.append(line)
    # Pattern 2: st.markdown after '# Visualisation' should also be 20 spaces
    elif i > 0 and '# Visualisation' in lines[i-1] and line.strip().startswith('st.markdown'):
        if line.strip().startswith('st.markdown(f"<h5'):
            # This one should be 20 spaces
            if not line.startswith('                    '):
                fixed_line = '                    ' + line.lstrip()
                fixed_lines.append(fixed_line)
                corrections.append(f"Line {i+1}: Fixed indentation for visualization header")
            else:
                fixed_lines.append(line)
        elif not line.startswith('                    '):  # For the HTML block
            fixed_line = '                    ' + line.lstrip()
            fixed_lines.append(fixed_line)
            corrections.append(f"Line {i+1}: Fixed indentation for visualization block")
        else:
            fixed_lines.append(line)
    else:
        fixed_lines.append(line)
    
    i += 1

# Write corrected file
with open('app.py', 'w') as f:
    f.writelines(fixed_lines)

print(f"Applied {len(corrections)} corrections")
for corr in corrections[:10]:  # Show first 10
    print(f"  - {corr}")

import subprocess
result = subprocess.run(['python', '-m', 'py_compile', 'app.py'], capture_output=True, text=True)
if result.returncode == 0:
    print("\n✅ SUCCESS - File compiles!")
else:
    print(f"\n❌ Still has errors:\n{result.stderr}")

