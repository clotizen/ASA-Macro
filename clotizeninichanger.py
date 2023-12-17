import tkinter as tk
from tkinter import ttk
import pyperclip
import configparser

class CheckBoxApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CloTiZen ini Changer")

        # 스타일 적용
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("TCheckbutton", background="#ececec")
        self.style.configure("TFrame", background="#ececec")
        self.style.configure("TButton", background="#4CAF50", foreground="white")
        self.style.configure("TCheckbutton", background="#ececec")
        self.style.configure("TLabel", background="#ececec")

        # 체크박스와 그에 해당하는 텍스트
        self.checkbox_vars = []
        self.texts = [
            "show fps",
            "show unit",
            "Remove Night(tree bright)",
            "Disable Remove Night",
            "Clear Shadow",
            "Disable Clear Shadow",
            "Clear Grass",
            "Disable Clear Gress",
            "Clear Cloud",
            "Disable Clear Cloud",
            "Clear Sky",
            "Disable Clear Sky",
            "Clear water only:",
            "Disable Clear Water only",
            "Colour in cave",
            "Disable Colour in cave",
            "Removes water top",
            "Remake water top",
            "Colour in cave",
            "Disable Colour in cave",
            "No Trees (derender)",
            "Disable No Trees (derender)",
            "No Debries",
            "Disable No Debries",
            "Farming",
            "Disable Farming",
            "Old ark ini",
            "Disable Ark old ini",
            "All in One ini",
            "Disable ALL in One ini",
            "Clotizen ini",
            "Cant Disable",
            "Broken Scout",
            "Fix Broken Scout"
        ]

        # 설정 파일 생성 또는 불러오기
        self.config = configparser.ConfigParser()
        self.config_file = "checkbox_app_config.ini"

        if self.config.read(self.config_file):
            # 파일이 있으면 체크박스 상태 읽어오기
            checkbox_states = self.config.get("Settings", "CheckboxStates").split(",")
            self.checkbox_vars = [tk.IntVar(value=int(state)) for state in checkbox_states]

        frame = ttk.Frame(master, padding="10")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

        # 체크박스 초기 위치 설정
        cb_x, cb_y = 0, 0  # 시작 위치 (수정 가능)

        for i, text in enumerate(self.texts):
            var = self.checkbox_vars[i] if i < len(self.checkbox_vars) else tk.IntVar()
            self.checkbox_vars.append(var)

            # 체크박스에 대한 라벨
            cb = ttk.Checkbutton(frame, variable=var, text=text)
            cb.grid(row=cb_y, column=cb_x, sticky=tk.W)

            # 위치 업데이트
            cb_x += 1
            if cb_x > 1:  # 한 줄에 2개씩 배치하도록 조절 (수정 가능)
                cb_x = 0
                cb_y += 1

        # 적용 버튼
        apply_button = ttk.Button(frame, text="Apply", command=self.apply_selection)
        apply_button.grid(row=cb_y, column=1, columnspan=2, pady=10)
        # 텍스트박스 추가 부분
        self.textbox_var = tk.StringVar(value="Contact CloTiZen.")
        textbox = ttk.Entry(frame, textvariable=self.textbox_var)
        textbox.grid(row=cb_y, column=0, pady=10)

    def apply_selection(self):
        selected_commands = [self.get_command(i) for i, var in enumerate(self.checkbox_vars) if var.get() == 1 and i < len(self.texts)]

        # 클립보드에 복사
        if selected_commands:
            joined_commands = " | ".join(selected_commands)
            pyperclip.copy(joined_commands)
            print("선택된 명령어:\n" + joined_commands)
        else:
            pyperclip.copy("")  # 선택된 명령어가 없을 경우 클립보드 비우기
            print("아무것도 선택되지 않았습니다.")

        # 체크박스 상태를 설정 파일에 저장
        checkbox_states = [var.get() for var in self.checkbox_vars]
        self.config["Settings"] = {"CheckboxStates": ",".join(map(str, checkbox_states))}
        with open(self.config_file, "w") as configfile:
            self.config.write(configfile)

    def get_command(self, index):
        commands = [
            "stat fps",
            "stat unit | stat unitgraph",
            "r.Shading.FurnaceTest 1",
            "r.Shading.FurnaceTest 0",
            "r.shadowquality 0",
            "r.shadowquality 1",
            "grass.Enable 0",
            "grass.Enable 1",
            "r.VolumetricCloud 0",
            "r.VolumetricCloud 1",
            "r.SkyAtmosphere 0",
            "r.SkyAtmosphere 1",
            "r.PostProcessing.DisableMaterials 1",
            "r.PostProcessing.DisableMaterials 0",
            "r.Lumen.DiffuseIndirect.Allow 1",
            "r.Lumen.DiffuseIndirect.Allow 0",
            "r.Water.SingleLayer 0",
            "r.Water.SingleLayer 1",
            "r.Lumen.DiffuseIndirect.Allow 1",
            "r.Lumen.DiffuseIndirect.Allow 0",
            "wp.Runtime.UpdateStreamingSources 0 | wp.Runtime.HLOD 0",
            "wp.Runtime.UpdateStreamingSources 1 | wp.Runtime.HLOD 1",
            "ark.MaxActiveDestroyedMeshGeoCollectionCount 0",
            "ark.MaxActiveDestroyedMeshGeoCollectionCount 1",
            "r.volumetricfog 0 | r.volumetriccloud 0 | grass.enable 0 | r.shadowquality 0 | r.materialqualitylevel 2 | ark.MaxActiveDestroyedMeshGeoCollectionCount 0",
            "r.volumetricfog 1 | r.volumetriccloud 1 | grass.enable 1 | r.shadowquality 1 | r.materialqualitylevel 15 | ark.MaxActiveDestroyedMeshGeoCollectionCount 1",
            "grass.Enable 0 | r.Water.SingleLayer.Reflection 0 | r.LightShaftQuality 0 | r.VolumetricCloud 0 | r.Shadow.Virtual.Enable 0 | r.Shadow.CSM.MaxCascades 0 | wp.Runtime.HLOD 0 | r.Water.SingleLayer.Reflection 0 | r.Lumen.DiffuseIndirect.Allow 1 | r.Shading.FurnaceTest 1 | r.PostProcessing.DisableMaterials 1",
            "grass.Enable 1 | r.Water.SingleLayer.Reflection 1 | r.LightShaftQuality 1 | r.VolumetricCloud 1 | r.Shadow.Virtual.Enable 1 | r.Shadow.CSM.MaxCascades 1 | wp.Runtime.HLOD 1 | r.Water.SingleLayer.Reflection 1 | r.Lumen.DiffuseIndirect.Allow 0 | r.Shading.FurnaceTest 0 | r.PostProcessing.DisableMaterials 0",
            "grass.Enable 0 | r.Water.SingleLayer.Reflection 0 | r.LightShaftQuality 0 | r.shadowquality 0 | r.VolumetricCloud 0 | r.VolumetricFog 0 | r.BloomQuality 0 | r.Lumen.Reflections.Allow 0 | r.Lumen.DiffuseIndirect.Allow 0 | r.Shadow.Virtual.Enable 0 | r.DistanceFieldShadowing 0 | r.Shadow.CSM.MaxCascades 1 | sg.FoliageQuality 0 | sg.TextureQuality 0 | show InstancedFoliage | show InstancedStaticMeshes | show DynamicShadows | show InstancedGrass | wp.Runtime.HLOD 1",
            "grass.Enable 1 | r.Water.SingleLayer.Reflection 1 | r.LightShaftQuality 1 | r.shadowquality 1 | r.VolumetricCloud 1 | r.VolumetricFog 1 | r.BloomQuality 1 | r.Lumen.Reflections.Allow 1 | r.Lumen.DiffuseIndirect.Allow 1 | r.Shadow.Virtual.Enable 1 | r.DistanceFieldShadowing 1 | r.Shadow.CSM.MaxCascades 0 | sg.FoliageQuality 1 | sg.TextureQuality 1 | show InstancedFoliage | show InstancedStaticMeshes | show DynamicShadows | show InstancedGrass | wp.Runtime.HLOD 0",
            "r.Streaming.PoolSize | 0 r.SkyAtmosphere 0 | r.VolumetricCloud 0 | r.Nanite.MaxPixelsPerEdge 4 | r.Lumen.ScreenProbeGather.RadianceCache.ProbeResolution 16 | r.DynamicGlobalIlluminationMethod 2 | r.ShadowQuality 0 | r.Water.SingleLayer.Reflection 0 | show InstancedGrass | show InstancedStaticMeshes | grass.Enable 0 | wp.Runtime.HLOD 0 | grass.Enable 0 | r.Water.SingleLayer.Reflection 0 | r.LightShaftQuality 0 | r.VolumetricCloud 0 | r.Shadow.Virtual.Enable 0 | r.Shadow.CSM.MaxCascades 0 | wp.Runtime.HLOD 0 r.Water.SingleLayer.Reflection 0 | r.Shading.FurnaceTest 0 | r.PostProcessing.DisableMaterials 1 | sg.FoliageQuality 0  | r.VolumetricCloud 0 | r.Water.SingleLayer.Reflection 0 | r.shadowquality 0 | r.ContactShadows 0 | grass.enable 0 | r.depthoffieldquality 0 | r.fog 0 | r.Water.SingleLayer 0 | show InstancedFoliage | show InstancedGrass | show InstancedStaticMeshes | r.lightshafts 0 | r.bloomquality 0  | r.LightCulling.Quality 0 | r.SkyAtmosphere 0 | sg.FoliageQuality 0 | r.VolumetricCloud 0 | r.Water.SingleLayer.Reflection 0 | r.shadowquality 0 | r.ContactShadows 0 |grass.enable 0 | r.depthoffieldquality 0 | r.fog 0 r.Water.SingleLayer 0 | show InstancedGrass | show InstancedStaticMeshes | r.lightshafts 0 | r.bloomquality 0 | r.LightCulling.Quality 0 r.SkyAtmosphere 0 | r.Lumen.Reflections.Allow 0 | r.Lumen.DiffuseIndirect.Allow 0 | r.Shadow.Virtual.Enable 0| r.DistanceFieldShadowing 0| r.Shadow.CSM.MaxCascades 0 |r.MipMapLODBias 1 | r.Shadow.CSM.MaxCascades 0 | r.PostProcessing.DisableMaterials 1r.VolumetricFog 0 | sg.GlobalIlluminationQuality 1 | r.SkylightIntensityMultiplier 3 | r.Shadow.Virtual.Enable 0 | r.Shadow.CSM.MaxCascades 0 | r.DistanceFieldShadowing 1 | r.ContactShadows 0 | wp.Runtime.HLOD 0 | grass.Enable 0 | r.Nanite.MaxPixelsPerEdge 1 | r.PostProcessing.DisableMaterials 1",
            "",
            "r.VolumetricCloud 0 | r.SkyAtmosphere 0 | r.PostProcessing.DisableMaterials 1 | r.Lumen.DiffuseIndirect.Allow 1 | r.Water.SingleLayer 0 | r.Lumen.DiffuseIndirect.Allow 1 | wp.Runtime.UpdateStreamingSources 0 | wp.Runtime.HLOD 0 | ark.MaxActiveDestroyedMeshGeoCollectionCount 0 | r.volumetricfog 0 | r.volumetriccloud 0 | grass.enable 0 | r.shadowquality 0 | r.materialqualitylevel 2 | ark.MaxActiveDestroyedMeshGeoCollectionCount 0 | grass.Enable 0 | r.Water.SingleLayer.Reflection 0 | r.LightShaftQuality 0 | r.VolumetricCloud 0 | r.Shadow.Virtual.Enable 0 | r.Shadow.CSM.MaxCascades 0 | wp.Runtime.HLOD 0 | r.Water.SingleLayer.Reflection 0 | r.Lumen.DiffuseIndirect.Allow 1 | r.Shading.FurnaceTest 1 | r.PostProcessing.DisableMaterials 1",
            "r.VolumetricCloud 1 | r.SkyAtmosphere 1 | r.PostProcessing.DisableMaterials 0 | r.Lumen.DiffuseIndirect.Allow 0 | r.Water.SingleLayer 1 | r.Lumen.DiffuseIndirect.Allow 0 | wp.Runtime.UpdateStreamingSources 1 | wp.Runtime.HLOD 1  | ark.MaxActiveDestroyedMeshGeoCollectionCount 1 | r.volumetricfog 1 | r.volumetriccloud 1 | grass.enable 1 | r.shadowquality 1 | r.materialqualitylevel 15 | ark.MaxActiveDestroyedMeshGeoCollectionCount 1 | grass.Enable 1 | r.Water.SingleLayer.Reflection 1 | r.LightShaftQuality 1 | r.VolumetricCloud 1 | r.Shadow.Virtual.Enable 1 | r.Shadow.CSM.MaxCascades 1 | wp.Runtime.HLOD 1 | r.Water.SingleLayer.Reflection 1 | r.Lumen.DiffuseIndirect.Allow 0 | r.Shading.FurnaceTest 0 | r.PostProcessing.DisableMaterials 0"
        ]
        return commands[index]


if __name__ == "__main__":
    root = tk.Tk()
    app = CheckBoxApp(root)
    root.mainloop()
