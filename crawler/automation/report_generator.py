import os
import yaml

class JekyllReportGenerator:
    def __init__(self, output_dir="content/reports/"):
        self.output_dir = output_dir

    def generate_report(self, all_gaps):
        # all_gaps is a list of {file: path, gaps: [...]}
        os.makedirs(self.output_dir, exist_ok=True)
        
        report_path = os.path.join(self.output_dir, "library_health.md")
        
        with open(report_path, 'w') as f:
            f.write("---\n")
            f.write("layout: page\n")
            f.write("title: Documentation Health Report\n")
            f.write("permalink: /reports/health/\n")
            f.write("---\n\n")
            
            f.write("# Documentation Health Library\n\n")
            f.write("| File | Issue Count | Top Severity |\n")
            f.write("| --- | --- | --- |\n")
            
            for item in all_gaps:
                file_name = os.path.basename(item['file'])
                issue_count = len(item['gaps'])
                severities = [g['severity'] for g in item['gaps']]
                top_severity = "High" if "High" in severities else ("Medium" if "Medium" in severities else "Low")
                
                f.write(f"| {file_name} | {issue_count} | {top_severity} |\n")
            
            f.write("\n\n*Last updated via automated audit workflow.*\n")
            
        print(f"Report generated: {report_path}")
