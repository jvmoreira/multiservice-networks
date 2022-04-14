import React, { ChangeEvent, ReactElement, useCallback, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { ChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorColorAwareField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const isColorAwareEnabled = useMemo(() => {
    return Boolean(singleRateThreeColorParameters.color_aware);
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorColorAware = useSetNfvTeFunctionParameter('color_aware', setSingleRateThreeColorParameters);

  const onSingleRateThreeColorColorAwareChangeHandler = useCallback((evt: ChangeEvent<HTMLInputElement>) => {
    setSingleRateThreeColorColorAware(evt.target.checked ? '1': undefined);
  }, [setSingleRateThreeColorColorAware]);

  return (
    <FormInput
      label="Color Aware"
      name="color-aware"
      type="checkbox"
      checked={isColorAwareEnabled}
      onChange={onSingleRateThreeColorColorAwareChangeHandler as ChangeHandler}
    />
  );
}
