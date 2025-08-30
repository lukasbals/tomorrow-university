from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from xgboost import XGBRegressor

class TreeEnsembleProject:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.results = {}
        self.best_model = None
        
    def run_baseline_comparison(self):
        """Compare baseline tree ensemble models"""
        models = {
            'Decision Tree': DecisionTreeRegressor(max_depth=10, random_state=42),
            'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
            'Extra Trees': ExtraTreesRegressor(n_estimators=100, random_state=42),
            'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42),
            'XGBoost': XGBRegressor(n_estimators=100, random_state=42)
        }
        
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        
        for name, model in models.items():
            # Cross-validation
            cv_scores = cross_val_score(model, X_train, y_train, cv=5)

            # Test performance
            model.fit(X_train, y_train)
            test_score = model.score(X_test, y_test)
            
            self.results[name] = {
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'test_score': test_score,
                'model': model
            }
            
            print(f"{name}: CV {cv_scores.mean():.3f}±{cv_scores.std():.3f}, Test {test_score:.3f}")
    
    def select_best_model(self):
        """Identify best performing model"""
        best_cv_score = max(self.results.keys(), key=lambda k: self.results[k]['cv_mean'])
        self.best_model = self.results[best_cv_score]['model']
        print(f"\nBest model: {best_cv_score}")
        return best_cv_score
    
    def generate_report(self):
        """Generate comprehensive project report"""
        print("\n" + "="*50)
        print("TREE ENSEMBLE PROJECT SUMMARY")
        print("="*50)
        
        # Performance ranking
        sorted_models = sorted(self.results.items(), key=lambda x: x[1]['cv_mean'], reverse=True)
        
        print("\nModel Rankings (by CV performance):")
        for i, (name, results) in enumerate(sorted_models, 1):
            print(f"{i}. {name}: {results['cv_mean']:.3f}±{results['cv_std']:.3f}")
        
        # Best model details
        best_name = sorted_models[0][0]
        best_results = sorted_models[0][1]
        
        print(f"\nRecommended Model: {best_name}")
        print(f"Cross-validation R²: {best_results['cv_mean']:.3f}")
        print(f"Test R²: {best_results['test_score']:.3f}")
        
        print(f"\nKey Findings:")
        print(f"• Best performing approach: {best_name}")
        print(f"• Performance stability: {best_results['cv_std']:.3f} CV standard deviation")
        print(f"• Generalization gap: {abs(best_results['cv_mean'] - best_results['test_score']):.3f}")
