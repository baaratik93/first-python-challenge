<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>358</width>
    <height>483</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <layout class="QGridLayout" name="gridLayout">
   <item row="0" column="0">
    <widget class="QFrame" name="frame">
     <property name="styleSheet">
      <string notr="true">background-color:rgb(106, 171, 255)</string>
     </property>
     <property name="frameShape">
      <enum>QFrame::StyledPanel</enum>
     </property>
     <property name="frameShadow">
      <enum>QFrame::Raised</enum>
     </property>
     <layout class="QFormLayout" name="formLayout">
      <item row="0" column="0" colspan="2">
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <widget class="QPushButton" name="pushButton">
          <property name="text">
           <string>Accueil</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="pushButton_2">
          <property name="text">
           <string>Clients</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="pushButton_3">
          <property name="text">
           <string>Assurances</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="pushButton_4">
          <property name="text">
           <string>Voitures</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
