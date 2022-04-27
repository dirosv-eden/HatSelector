# Hat Selector (หมวกคัดสรร)
หมวกคัดสรร เป็นโปรแกรมที่ใช้สำหรับคัดเด็กนักเรียนเข้าบ้าน โดยบ้านทั้งหมดจะมีอยู่ 4 หลัง ซึ่งแต่ละหลังจะต้องมีจำนวนนักเรียนที่ไม่ห่างกันมาก

### วิธีการเลือกคน
แปลง String เป็นตัวเลขแล้ว แล้วบวกด้วยค่าสุ่มค่าใดค่าหนึ่ง แล้ว mod ด้วยจำนวนบ้าน
เด็กหนึ่งคนจะได้บ้านที่เหมาะสม หากบ้านใดมีคนอยู่เยอะแล้ว จะถูกคัดเลือกไปยังบ้านที่มีคนน้อย




### Requirements 
<ul>
 <li>Python 3.9.x</li>
</ul>

### Run App.
<ol>
 <li>สำหรับเครื่องที่ไม่มี virtualenv สามารถติดตั้งได้โดยคำสั่ง : <code>pip install virtualenv </code> </li>
<li> สร้าง virtual environments : <code>virtual venv </code>.</li>  
<li> เข้าใช้ทรัพยากร สำหรับ Mac/Linux : <code>source venv/bin/activate</code>, สำหรับ Windows <code> venv/Scripts/activate.bat </code></li>
<li> ติดตั้ง package : <code>pip install -r requirements.txt</code></li>
<li> Run app : <code>python hatselector.py</code></li>
</ol>
